import imageAnalyzer
import mazeAnalyzer

matrix = imageAnalyzer.read_bmp('Maze5x5PNG.png')

result = mazeAnalyzer.AStarAlgorithm(matrix=matrix)

print(result)
        
