import math
def sign(x): #обычный сигнум
    if x>0:
        return 1
    elif x<0:
        return -1
    else:
        return 0
def right_and_left(list): # разделение на правую и левую часть от "центральной" линии
    right=[]
    left=[]
    max=list[0][0]
    min=list[0][0]
    P_max=list[0]
    P_min=list[0]
    for x in list:
        if x[0]>max:
            max=x[0]
            P_max=x
        if x[0]<min:
            min=x[0]
            P_min=x
    for x in list:
        if sign((0-5)*(x[1]-0)-(0-0)*(x[0]-5))==1:
            right.append(x)
        elif sign((0-5)*(x[1]-0)-(0-0)*(x[0]-5))==(-1):
            left.append(x)
    return max,min,left,right,P_min,P_max
Max,Min,Left,Right,p_min,p_max=right_and_left([[0,0],[1,-2],[3,2],[3,7],[4,-2],[4,4],[5,-5],[5,7],[6,0],[6,3],[7,5],[8,6],[9,-7],[10,4],[11,0]])

def algoritm(left,max,min):algoritm """старое название upper_hull_2. было такое название из-за того
                                    что это вторая попытка написать код  для обхода сверху
                                    а в итоге получилось сделать и для нижнего обхода"""
    if left == []: #если список закончился то возращает пустой масив
        A = []
        return []
    Point=left[0]
    max_point=0

    for x in left: # обход по списску
        A=min[0]*max[1]+x[0]*min[1]+max[0]*x[1]-x[0]*max[1]-max[0]*min[1]-min[0]*x[1]

        if A > max_point: # сравнение с максимальным елементом
            Point=x
            max_point=A
        if sign(A)<0:
            continue
        if A==max_point: # проверка какая из точок лежит дальше если елемент совпадает с максимальным
            A = [x[0] - min[0], x[1] - min[1]]
            B = [max[0] - min[0], max[1] - min[1]]
            cos1 = ((A[0]) * (B[0]) + (A[1] * B[1])) / ( math.sqrt(A[0] ** 2 + A[1] ** 2) * math.sqrt(B[0] ** 2 + B[1] ** 2))
            C = [Point[0] - min[0], Point[1] - min[1]]
            cos2 = ((C[0]) * (B[0]) + (C[1] * B[1])) / ( math.sqrt(C[0] ** 2 + C[1] ** 2) * math.sqrt(B[0] ** 2 + B[1] ** 2))
            if cos1 < cos2:
                Point = x
                max_point = A
    All=[]
    Left = [Point] + algoritm(left[0:left.index(Point)], Point, min) # рекурсивное продолжение поиска точек, от найденой точки, с левой стороны
    Right = [Point] + algoritm(left[(left.index(Point) + 1):], max, Point)# такое же рекурсивное продолжение но уже с правой стороны
    Right = Right + [max]
    for x in Right: # прооверка на одинаковые елменты в списках
        if x in All:
            continue
        for y in Left:

            if x == y:
                All.append(x)
                break
            else:
                All.append(x)
                break
    return [min] + All # возвращение списка всех найдених точек на даный момент



def my_sum(list): #функция которая считает длину оболочки
    sum=0
    for x in range(len(list)-1):
        sum+=math.sqrt((list[x+1][0]-list[x][0])**2+(list[x+1][1]-list[x][1])**2)
    return sum
print(my_sum(algoritm(Left,p_max,p_min))+my_sum(algoritm(Right,p_max,p_min)))
