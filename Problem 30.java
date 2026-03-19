// Divide Two Integers

class Solution {
    public int divide(int dividend, int divisor) {
        // Special Case: Overflow for -2^31 / -1
        if (dividend == Integer.MIN_VALUE && divisor == -1) {
            return Integer.MAX_VALUE;
        }

        // Determine the sign of the result
        boolean isNegative = (dividend < 0) ^ (divisor < 0);

        // Convert to long to handle the absolute value of Integer.MIN_VALUE
        long absDividend = Math.abs((long) dividend);
        long absDivisor = Math.abs((long) divisor);

        int quotient = 0;

        // Exponential subtraction
        while (absDividend >= absDivisor) {
            long tempDivisor = absDivisor;
            long multiple = 1;

            // Double the divisor until it's larger than the dividend
            while (absDividend >= (tempDivisor << 1)) {
                tempDivisor <<= 1;
                multiple <<= 1;
            }

            // Subtract the largest found multiple of the divisor
            absDividend = absDividend - tempDivisor;
            quotient += multiple;
        }

        return isNegative ? -quotient : quotient;
    }
}
