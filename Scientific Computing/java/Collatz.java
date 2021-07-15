public class Collatz {
    public static void main(String[] args) {
        final long N = 1000 * 1000 ;
        for(long i = 1; i <= N; i++) {
            System.out.println("i = " + i + " - " + GetCollatzSequenceCount(i));
        }
        System.out.println("Done!");
    }

    private static long GetCollatzSequenceCount(long n){
        if (n <= 0) return 0;
        long count = 0;
        while(true){
            if (n == 1) return count;
            if (n % 2 == 0) {
                n /= 2;
            } else {
                n = n * 3 + 1;
            }
            count++;
        }
    }
}

