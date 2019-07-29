# --------------------------------------------------------------------------- #
# --------------------------------------------------------------------------- #
def get_3d_measures(file, indexEasting, indexNorthing, indexElevation):

    import math

    # Get x, y, z data
    # ----------------
    centerlineData = []
    for row in file:
        a = row.split(',')
        centerlineData.append(a)    

    # Append 3D Measures
    # ------------------
    length_3d = []
    measure_3d = []
    measure = 0.0
    measure_3d.append(measure)
    easting = []
    northing = []
    easting.append( float(centerlineData[0][indexEasting ]))
    northing.append(float(centerlineData[0][indexNorthing]))

    for i in range(1,len(centerlineData)):

        x1 = float(centerlineData[i-1][indexEasting ])
        y1 = float(centerlineData[i-1][indexNorthing])
        x2 = float(centerlineData[i  ][indexEasting ])
        y2 = float(centerlineData[i  ][indexNorthing])

        # Find length  d2  between (x2,y1) and (x1,y1). This distance  d2  is
        # added to the 2D chainage value  d2New  .
        projectedDistance = 0 # Not calculating the x,y at a projected distance
        [s, d2, p, t, dx, dy] = calculate_next_coordinates(x1, x2, y1, y2, projectedDistance)

        elv1 = float(centerlineData[i-1][indexElevation])
        elv2 = float(centerlineData[i  ][indexElevation])

        [s,d3,newZvalue] = slope_distance(elv1, elv2, d2, projectedDistance)
        measure = measure + d3

        length_3d.append(d3)
        measure_3d.append(measure)

        easting.append(x2)
        northing.append(y2)

    # Create Output List
    # ------------------
    outputList = []
    for i in range(len(easting)):
        outputList.append((easting[i],northing[i],float(centerlineData[i][indexElevation]),measure_3d[i]))

    return outputList

# --------------------------------------------------------------------------- #
# --------------------------------------------------------------------------- #
