class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        return self.__method1(version1, version2)

    def __method1(self, version1: str, version2: str) -> int:
        version1Array = version1.split(".")
        version2Array = version2.split(".")

        version1Length = len(version1Array)
        version2Length = len(version2Array)

        i = 0
        while i < version1Length or i < version2Length:
            n1 = int(version1Array[i]) if i < version1Length else 0
            n2 = int(version2Array[i]) if i < version2Length else 0

            if n1 > n2:
                return 1
            elif n1 < n2:
                return -1
            else:
                i += 1

        return 0
