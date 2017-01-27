# -*- coding: utf-8 -*-
"""
Created on Wed Jan 18 09:39:53 2017

@author: mrichardson
"""

import parameters as params
import point
import math

def print_message(message):
    if params.DEBUG > 0:
        print(message)
        
def calculateVector(p1, p2):
    return point.Point((p1.getX() - p2.getX()), (p1.getY() - p2.getY()))
        
def dot_product(u, v):
    return u.getX()*v.getX() + u.getY()*v.getY()
    
def cross_product(u, v):
    return u.getX()*v.getY() - u.getY()*v.getX()
    
def calculateRho(u):
    return math.sqrt(math.pow(u.getX(), 2) + math.pow(u.getY(), 2))
    
def calculateR(rho, rhoDash, phi, phiDash):
    return math.sqrt(math.pow(rho, 2) + math.pow(rhoDash, 2) - 2*rho*rhoDash*math.cos(phi - phiDash));

def isZero(num):
    if num < params.ZERO and num > -params.ZERO:
        return 0
    else:
        return num
        
def greaterThanZero(num):
    if num > -params.ZERO:
        return True
    else:
        return False
        
def roundNumbers(num):
    return round(num, 6)
    
def calculateGradient(p1, p2):
    if (p1.getX() - p2.getX()) == 0:
        return float("inf")
    return ((p1.getY() - p2.getY())/(p1.getX() - p2.getX()))
    
def calculateC(p, m):
    if m == float("inf"):
        return p.getX()
    return (p.getY() - m*p.getX())
    
def calculateDistance(p1, p2):
    return math.sqrt(math.pow((p1.getX() - p2.getX()), 2) + math.pow((p1.getY() - p2.getY()), 2))
    
def calculateXIntercept(obs_m, tmp_m, obs_c, tmp_c):
    return ((obs_c - tmp_c)/(tmp_m - obs_m))
    
def calculateYIntercept(x, m, c):
    return m*x + c
    
def isPointInsideTriangle(obs, start, end, intercept):
    p1x = obs.getX()
    p1y = obs.getY()
    
    p2x = start.getX()
    p2y = start.getY()
    
    p3x = end.getX()
    p3y = end.getY()
    
    px = intercept.getX()
    py = intercept.getY()
    
#    area = 0.5*(p1x*(p2y - p3y) + p2x*(p3y - p2y) +p3x*(p1y - p2y))
    
    alpha = ((p2y - p3y)*(px - p3x) + (p3x - p2x)*(py - p3y))/((p2y - p3y)*(p1x - p3x) + (p3x - p2x)*(p1y - p3y))
    beta = ((p3y - p1y)*(px - p3x) + (p1x - p3x)*(py - p3y))/((p2y - p3y)*(p1x - p3x) + (p3x - p2x)*(p1y - p3y))
    gamma = 1-alpha-beta
    
    check = greaterThanZero(alpha) and greaterThanZero(beta) and greaterThanZero(gamma)
    
    return check