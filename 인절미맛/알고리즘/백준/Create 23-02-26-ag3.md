```java
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.List;

class Main{
     public static void main(String[] args) throws IOException  {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		String[] str= br.readLine().split(" ");
		List<String> list =  Arrays.asList(str);
		int cnt = 0;
		int max = 0;
		int check = 1;
		
		int result =0;
		
		int ifirst = Integer.parseInt(list.get(0));
		int isecond = Integer.parseInt(list.get(1));
		for (int a =0 ;a<list.size();a++) {
			Integer i = Integer.parseInt(list.get(a));
			if(max<i) {
				max =i;
			}
		
			for (int b =a+1 ;b<list.size();b++) {
				Integer j = Integer.parseInt(list.get(b));
				if(i.equals(j) ) {
					
					if(a == 1 && ifirst == isecond) {
						continue;
					}
					
					check++;
					cnt = i;
				}
			}
		}
		if(check ==3) {
			result = 10000 + cnt * 1000;
		}else if(check ==2) {
			result = 1000 + cnt * 100;
		}else {
			result = max * 100;
		}
		
		System.out.println(result);
     }
 }
```
