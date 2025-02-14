class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        for el in image:
            el = el.reverse()

        for i in range(len(image)):
            image[i] = [1 if el == 0 else 0 for el in image[i] ]

        return image
