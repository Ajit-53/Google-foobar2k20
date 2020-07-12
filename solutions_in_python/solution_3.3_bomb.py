def solution(M, F):

    count = 0

    m = int(M)

    f = int(F)



    while m != 1 or f != 1:

        if m == 1 or f == 1:

            if m == 1:

                count += f - 1

            if f == 1:

                count += m - 1

            break



        if m < f:

            if m == 0:

                return "impossible"

            count += f / m

            f %= m

        else:

            if f == 0:

                return "impossible"

            count += m / f

            m %= f



    return str(count)