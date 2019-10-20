class Solution(object):
    def gardenNoAdj(self, N, paths):
        """
        :type N: int
        :type paths: List[List[int]]
        :rtype: List[int]
        """

        '''
        1. Use a list to store key i to [j1, j2, j3] link. Then I can search faster. list= [[] for x in range(N)]

        '''
        #FIXED index need to +1, the garden start from one
        #print('{} garden and len of paths {} .'.format(N, len(paths) ))  
        dict_path = [[] for x in range(N+1)]
        for i in range(len(paths)):
            x,y = paths[i]
            dict_path[x].append(y)
            dict_path[y].append(x)
            
        #print(dict_path)
        
        ##brute force to color then.
        #init color
        color = [0 for x in range(0, N+1)]
        for i in range(1, N+1):
            linked = dict_path[i] 
            #print('linked {} for i {}'.format(linked, i))
            #print('linked == [] ?? {}'.format(linked == []))
            if linked == []:
                color[i] = 1
            else: 
                check_color = [False, False,False,False, False]
                for j in range(0, len(linked) ):
                    one_color = color[ linked[j] ] 
                    if (one_color != 0):
                        check_color[one_color] = True
                for j in range(1,5):
                    if check_color[j] == False:
                        color[i] = j
                        break
                        
            #print( 'i = {}, color list: {}'.format(i, color[:i+1]) )

        return color[1:]
