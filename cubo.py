#Cubo rubik 3d

class Cube:
   def __init__(self):
       self.front = [[0]*3 for _ in range(3)]
       self.back = [[1]*3 for _ in range(3)]
       self.left = [[2]*3 for _ in range(3)]
       self.right = [[3]*3 for _ in range(3)]
       self.up = [[4]*3 for _ in range(3)]
       
       self.down = [[5]*3 for _ in range(3)]

   def rotate_face_clockwise(self, face):
       face[:] = [list(reversed(col)) for col in zip(*face)]

   def rotate_face_counter_clockwise(self, face):
       face[:] = [list(col)[::-1] for col in zip(*face)]
