import math
#self.rect_a = pygame.Rect(math.sqrt(16), y, 60, 60)
#math.sqrt(16)
def getrectsize(rect):
    rectatributes = vars(rect)
    rect_x = rectatributes[2]
    rect_y = rectatributes[3]
    return (rect_x, rect_y)
def getrect_xsize(rect):
    rectatributes = vars(rect)
    rect_x = rectatributes[2]
    return rect_x
def getrect_ysize(rect):
    rectatributes = vars(rect)
    rect_y = rectatributes[3]
    return rect_y
def middle(position, size):
    middlepoint = position - (size / 2)
    return middlepoint 

    