import java.util.HashMap;

/*
 * Count the number of ways a,b,c,d ∈ { 1,...,N } satisfy 
 * √(a^2 + b^2) == √(c^2 + d^2)
 */
public class VeevaChallenge {
    public static void main(String[] args) {
		final int N = 80;
		int solution = 0;

		// Brute Force Solution O(n^4)

		for (int a = 1; a <= N; a++) {
			for (int b = 1; b <= N; b++) {
				for (int c = 1; c <= N; c++) {
					for (int d = 1; d <= N; d++) {
						if (a * a + b * b == c * c + d * d) {
							solution++;
						}
					}
				}
			}
		}
		System.out.println("Brute force solution: " + solution);

		// Smarter Solution O(n^2)

		/* 
		1 LHS solution for number 2 
		1^2 + 1^2 == 2

		2 LHS solutions for number 5 
		1^2 + 2^2 == 5
		2^2 + 1^2 == 5

		3 LHS solutions for number 50 
		1^2 + 7^2 == 50
		7^2 + 1^2 == 50
		5^2 + 5^2 == 50
		*/

		solution = 0;
		HashMap<Integer, Integer> numToCount = new HashMap<>();
		for (int a = 1; a <= N; a++) {
			for (int b = 1; b <= N; b++) {
				int num = a * a + b * b;
				Integer count = numToCount.get(num);
				numToCount.put(num, count != null ? count + 1 : 1);
			}
		}
		for (Integer count : numToCount.values()) {
			solution += count * count;
		}
		System.out.println("Smarter solution: " + solution);
    }
}