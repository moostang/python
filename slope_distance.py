def slope_distance(baseElev, elv2, dist_betwn_baseElev_elv2, projectedDistance):

    # Calculate the slope and distance between two Cartesian points.
    #
    # Input:
    #   For 2-D graphs,
    #       dist_betwn_baseElev_elv2, Distance between two elevation points (FLOAT)
    #       baseElev,  Elevation of first cartesian point (FLOAT)
    #       elv2,  Elevation of second cartesian point (FLOAT)
    #
    # Output:
    #   For 2-D graphs/profiles,
    #   slope,    Slope betweewn two points. The horizontal plane is the
    #             plane of origin. Slope above and below the plane are
    #             positive and negative, respectively. This variable is
    #             needed for creating 2-D profiles/graphs.
    #   distance, Cartesian length between two points on a graph/profile.
    #             Used as 3-D Chainage distance (may differ from survey
    #             chainage data)
    #
    # Created: April 24, 2019 (moostang)

    import math

    numer = elv2 - baseElev # Numerator
    denom = dist_betwn_baseElev_elv2

    print(numer,denom)

    distance = math.sqrt( numer**2 + denom**2)

    # Check if denominator is zero, i.e. both points lies on the same
    # y-axis plane.
    # a. If denominator is zero, then determine if it lies on the
    #    upper (positive) or bottom (negative) y-axis plane.
    # b. If denominator is not zero, then proceed with normal pythagorean
    #    trigonometric calculations
    #

    if denom == 0:
        print("Denominator is zero")
        b = 0
        if elv2 > baseElev:
            print("    and elv2 > baseElev")
            p =  1 # Second point is above first point
            theta = math.pi/2
        elif elv2 < baseElev:
            print("    and elv2 < baseElev")
            p = -1 # Second point is below first point
            theta = - math.pi/2
        else:
            print("    and elv2 = baseElev. Both of them are the same points !")
            p = 0
            b = 0
            theta = 0
    else:
        print("Denominator is NOT zero")
        theta = math.atan(numer/denom)
        p = math.sin(theta)
        b = math.cos(theta)

    slope  = theta

    if projectedDistance != 0 and projectedDistance <= dist_betwn_baseElev_elv2:
        b = abs(projectedDistance) # Tackle negative distances (may occur)
        newElev = baseElev + b*math.tan(slope)
        distance = projectedDistance/math.cos(slope)
    else:
        newElev = elv2

    return slope, distance, newElev
