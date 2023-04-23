class Image:
    import cv2

    def __init__(self,image,imMask):
        self.image = image
        self.imMask = imMask

    def getImage(self):
        return self.image
    def getImMask(self):
        return self.imMask
        