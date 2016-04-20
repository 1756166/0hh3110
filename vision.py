#!/usr/bin/python
# -*- coding: utf-8 -*-

from PIL import Image

def get_coords():
    size = 12
    first = [680, 260]
    last = [1260, 830]
    BLUE = [[53, 184, 213], [48, 167, 194]] #Color image for vision "processing", for whatever reason there are two of each color
    RED =  [[213, 83, 54], [194, 75, 49]]
    BLACK = [[42, 42, 42]]
    coordinates = [[680+((last[0]-first[0])/(size-1))*i, 260+((last[1]-first[1])/(size-1))*j] for j in range(12) for i in range(12)] #For reading the picture
    try:
        im = Image.open("board.png")
    except:
        print "NO IMAGE FOUND"
    picture = im.load()
    board = [['0','0','0','0','0','0','0','0','0','0','0','0'],['0','0','0','0','0','0','0','0','0','0','0','0'],\
    ['0','0','0','0','0','0','0','0','0','0','0','0'],['0','0','0','0','0','0','0','0','0','0','0','0'],\
    ['0','0','0','0','0','0','0','0','0','0','0','0'],['0','0','0','0','0','0','0','0','0','0','0','0'],\
    ['0','0','0','0','0','0','0','0','0','0','0','0'],['0','0','0','0','0','0','0','0','0','0','0','0'],\
    ['0','0','0','0','0','0','0','0','0','0','0','0'],['0','0','0','0','0','0','0','0','0','0','0','0'],\
    ['0','0','0','0','0','0','0','0','0','0','0','0'],['0','0','0','0','0','0','0','0','0','0','0','0']] #I'm sorry
    for index, coordinate in enumerate(coordinates):
        color = list(picture[coordinate[0], coordinate[1]])
        first_index = index/12 #which row
        second_index = index%12 #which column
        if color in BLUE:
            board[first_index][second_index] = '2'
        elif color in RED:
            board[first_index][second_index] = '1'
        elif color in BLACK:
            board[first_index][second_index] = '0'
        else:
            print r"""                           #####
                         #########
                        ###########
                       #############
                      ###############
                      ###############
                      ###############
                      ###############
                       #############
                        ###########
            #####        ###########\
          ########        ############\
         ##########     ########     ##\
        ############   #########      # \
       ############## #########          |
       ########################      \   \
       ########################      o  o\\
       ########################     oo\ oo |    /###\
        ########################     oo  o |   /#`####
        ########################    \oo \o\ \__##`####
         ########## #####    ###     oo  oo /  #######
          ########  ###        ##  /~\o  \//   ######/
           #####    ##          #      \ /     \####/
                    ##                            |
                    ##    /\~~\                   |
                     #    | \                     |
                     #    |  \                   |
                      |       \                 |
                     ####      #               |
                    ######     ###           |~
                    #######   xxx##       / ~
                    #########  xxxxx####/~
                     ########  xxxxxx##\
                     ######\##  xxxxx#  \
                      ######\##       ###\
                      #######\###    #####\
                       #######|#######(((((((
                       #######\####))))))))))))
                        #######\##))))))))))88)))
                         #######))))))8888))8888)))
                         ######)))))))88888))888))))
                          #####))))))))8888)))88)))))
                          ####..))))))))88)))))))))))
                           ##...)))))))))))))))))))))
                           ##...)))))))))))))))))))))
                           #...))))))))))))))))))))))
                           #...))))))))))))))))))))))
                           ).)))))))))))))))))))))))
                            )--/)))))))))))))))))))
                             ))))))))))))))))))))#
                             ))))))))))))  ))))###
                               )))))))))     ####
                                #####  #    #####
                               #####   #    #####
                               #####   #    #####
                              ######   #    #####
                              #####   #     ####
                             ######   #    #####
                             #####    #    #####
               /9999\    /99######   #   99####99
              99999999999|99#####9   #  999###99999
             9999999\99999\999##999 #   99999999999-999
            999999999-99999\-99999##  999999999999/999999
           99999999999\--9999999999   9999999999/-999999999
           99999999999999\999999999  9999999999/999999999999
           99999999999999999999999     999999999999999999999
             9999999999999999999         999999999999999999
               999999999999999             99999999999999""" #shouldn't happen
    return board