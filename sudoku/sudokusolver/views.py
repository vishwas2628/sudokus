import cv2
import base64
import numpy as np
from io import BytesIO
from PIL import Image
from django.shortcuts import render
from django.http import HttpResponse
from sudokusolver.utlis import *
from . import solver

def image_to_sudoku_view(request):
    if request.method == "POST" and request.FILES.get("image"):
        uploaded_image = request.FILES["image"]

        # Load and prepare the image
        pil_image = Image.open(uploaded_image)
        img = cv2.cvtColor(np.array(pil_image), cv2.COLOR_RGB2BGR)
        heightImg, widthImg = 450, 450
        img = cv2.resize(img, (widthImg, heightImg))  # Resize image to 450x450
        imgBlank = np.zeros((heightImg, widthImg, 3), np.uint8)
        imgThreshold = preProcess(img)

        # Find contours
        contours, hierarchy = cv2.findContours(
            imgThreshold, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE
        )
        biggest, maxArea = biggestContour(contours)

        if biggest.size != 0:
            biggest = reorder(biggest)
            print(biggest)
            pts1 = np.float32(biggest)
            pts2 = np.float32([[0, 0], [widthImg, 0], [0, heightImg], [widthImg, heightImg]])
            matrix = cv2.getPerspectiveTransform(pts1, pts2)
            imgWarpColored = cv2.warpPerspective(img, matrix, (widthImg, heightImg))
            imgWarpColored = cv2.cvtColor(imgWarpColored, cv2.COLOR_BGR2GRAY)

            # Process Sudoku board
            model = intializePredectionModel()  # Load the CNN model
            boxes = splitBoxes(imgWarpColored)
            numbers = getPredection(boxes, model)
            numbers = np.asarray(numbers)
            posArray = np.where(numbers > 0, 0, 1)

            board = np.array_split(numbers, 9)
            print(board)
            if not solver.is_valid_sudoku(board):
                return render(request, "sudokusolver/sudoku_result.html", {"error": "No Sudoku Found as board"})
            
            solver.solveSudoku(board) #Using Hashing and backtracking
            

            flatList = [item for sublist in board for item in sublist]
            solvedNumbers = flatList * posArray
            imgSolvedDigits = displayNumbers(imgBlank.copy(), solvedNumbers)

            # Warp solution back to the original image
            imgInvWarpColored = cv2.warpPerspective(imgSolvedDigits, cv2.getPerspectiveTransform(pts2, pts1), (widthImg, heightImg))
            inv_perspective = cv2.addWeighted(imgInvWarpColored, 1, img, 0.5, 1)

            # Convert the final image to a format suitable for rendering
            result_image = Image.fromarray(cv2.cvtColor(inv_perspective, cv2.COLOR_BGR2RGB))
            buffer = BytesIO()
            result_image.save(buffer, format="PNG")
            result_image_base64 = base64.b64encode(buffer.getvalue()).decode()

            return render(request, "sudokusolver/sudoku_result.html", {"result_image": result_image_base64})
        else:
            return render(request, "sudokusolver/sudoku_result.html", {"error": "No Sudoku Found as image"})
    return render(request, "sudokusolver/upload_sudoku.html")
