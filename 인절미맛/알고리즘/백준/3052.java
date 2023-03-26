class test {
  /**
		 * 3052번 나머지
		 * 
		 * 입력 : 첫째 줄부터 열번째 줄 까지 숫자가 한 줄에 하나씩 주어진다. 
		 *       이 숫자는 1,000보다 작거나 같고, 음이 아닌 정수이다.
		 * 출력 : 첫째 줄에, 42로 나누었을 때, 서로 다른 나머지가 몇 개 있는지 출력한다.      
		 * 
		 * 
		 */
		
	public static void main(String[] args) throws IOException  {
  
  BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	java.util.HashMap<String, Integer> hm = new java.util.HashMap<String, Integer>();
	for (int i = 0; i < 10; i++) {
		Integer tmp = Integer.parseInt(br.readLine())%42;
			
		Object obj = hm.get(String.valueOf(tmp));
			
		if(obj ==null) {
			hm.put(String.valueOf(tmp), 1);
		}
	}
		
		
		System.out.println(hm.size());
		if(br !=null) {
			br.close();
		}
		
	}
		
}
