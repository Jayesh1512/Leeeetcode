class Solution(object):
    def floodFill(self, image, sr, sc, color):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type color: int
        :rtype: List[List[int]]
        """
        #bfs
        q = []
        oc = image[sr][sc]
        image[sr][sc] = color
        q.append((sr,sc))
        print(q)
        while(len(q) != 0):
            x,y = q.pop(0)
            if x+1 < len(image) and image[x+1][y] == oc and image[x+1][y] != color:
                image[x+1][y] = color
                q.append((x+1,y))

            if x-1 >=0 and image[x-1][y] == oc and image[x-1][y] != color:
                image[x-1][y] = color
                q.append((x-1,y))

            if y-1 >=0 and image[x][y-1] == oc and image[x][y-1] != color:
                image[x][y-1] = color
                q.append((x,y-1))

            if y+1 < len(image[0]) and image[x][y+1] == oc and image[x][y+1] != color:
                image[x][y+1] = color
                q.append((x,y+1))


        return image
