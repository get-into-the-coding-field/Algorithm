  /*  *****************************************************
   *
   * 2525번 오븐시계 
   * java 로 작성 
	 * 현재시각 정보: H,M 
	 * 요리에 필요한 시간 : Cook 0<1000
	 * M+Cook >= 60
	/* *****************************************************
	BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	StringTokenizer st = new StringTokenizer(br.readLine()," ");
	int iH = Integer.parseInt(st.nextToken());
	int iM = Integer.parseInt(st.nextToken());
	int iCook = Integer.parseInt(br.readLine());
	
	int cal1 = iH * 60 + iM;
	int tmp = cal1 + iCook;
	if(tmp  >=24 * 60) {
			
		int cal2 =  tmp - 24 * 60 ;
		
		System.out.println(cal2/60 + " " + cal2%60);
	}else {
		System.out.println(tmp/60 + " " + tmp%60);
	}
