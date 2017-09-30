
#-*- coding: utf-8 -*-
'''
python: www.iplaypy.com
@author: Jekey
欧几里得距离
如果数据很稠密，使用该算法较好
'''
import codecs
from math import sqrt

users = {"Angelica": {"Blues Traveler": 3.5, "Broken Bells": 2.0, "Norah Jones": 4.5, "Phoenix": 5.0, "Slightly Stoopid": 1.5, "The Strokes": 2.5, "Vampire Weekend": 2.0},
         "Bill":{"Blues Traveler": 2.0, "Broken Bells": 3.5, "Deadmau5": 4.0, "Phoenix": 2.0, "Slightly Stoopid": 3.5, "Vampire Weekend": 3.0},
         "Chan": {"Blues Traveler": 5.0, "Broken Bells": 1.0, "Deadmau5": 1.0, "Norah Jones": 3.0, "Phoenix": 5, "Slightly Stoopid": 1.0},
         "Dan": {"Blues Traveler": 3.0, "Broken Bells": 4.0, "Deadmau5": 4.5, "Phoenix": 3.0, "Slightly Stoopid": 4.5, "The Strokes": 4.0, "Vampire Weekend": 2.0},
         "Hailey": {"Broken Bells": 4.0, "Deadmau5": 1.0, "Norah Jones": 4.0, "The Strokes": 4.0, "Vampire Weekend": 1.0},
         "Jordyn":  {"Broken Bells": 4.5, "Deadmau5": 4.0, "Norah Jones": 5.0, "Phoenix": 5.0, "Slightly Stoopid": 4.5, "The Strokes": 4.0, "Vampire Weekend": 4.0},
         "Sam": {"Blues Traveler": 5.0, "Broken Bells": 2.0, "Norah Jones": 3.0, "Phoenix": 5.0, "Slightly Stoopid": 4.0, "The Strokes": 5.0},
         "Veronica": {"Blues Traveler": 3.0, "Norah Jones": 5.0, "Phoenix": 4.0, "Slightly Stoopid": 2.5, "The Strokes": 3.0}
        }

#Minkowski 距离
def minkowski(rate1,rate2,r):
    distance = 0
    commonRating = False
    for key in rate1:
        if key in rate2:
            distance+=pow(abs(rate1[key]-rate2[key]),r)
            commonRating=True
    if commonRating:
        return pow(distance,1/r)
    else:
        return -1
    
#返回最近距离用户
def computeNearestNeighbor(username,users):
    distances = []
    for key in users:
        if key<>username:
            distance = minkowski(users[username],users[key],2)
            distances.append((distance,key)) 
    distances.sort()          
    return distances

#推荐
def recommend(username,users):
    #获得最近用户的name
    nearest = computeNearestNeighbor(username,users)[0][1]
    recommendations =[]
    #得到最近用户的推荐列表
    neighborRatings = users[nearest]
    for key in neighborRatings:
        if not key in users[username]:
            recommendations.append((key,neighborRatings[key]))
    recommendations.sort(key=lambda rat:rat[1], reverse=True)
    return recommendations 
    
if __name__ == '__main__':
    print recommend('Hailey', users)

