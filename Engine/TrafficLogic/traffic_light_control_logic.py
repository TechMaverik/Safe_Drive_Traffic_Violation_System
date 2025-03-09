class ControlTraffic:
    def control_traffic(self, j1, j2, j3, j4):
        if j1 > j2 and j1 > j3 and j1 > j4:
            j1 = True
            j2 = False
            j3 = False
            j4 = False

        elif j2 > j1 and j2 > j3 and j2 > j4:
            j2 = True
            j1 = False
            j3 = False
            j4 = False

        elif j3 > j1 and j3 > j2 and j3 > j4:
            j3 = True
            j1 = False
            j2 = False
            j4 = False

        elif j4 > j1 and j4 > j3 and j4 > j2:
            j4 = True
            j1 = False
            j3 = False
            j2 = False

        elif j1 == j2 and j1 == j3 and j1 == j4:
            j1 = True
            j2 = False
            j3 = False
            j4 = False

        else:
            j1 = False
            j2 = False
            j3 = False
            j4 = False

        return j1, j2, j3, j4
