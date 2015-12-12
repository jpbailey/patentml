			for (Entry<Patent, TreeMap<String, Integer>> otherPatent : dictionary
					.entrySet()) {
				double sum = 0;
				for (Entry<String, Integer> myPatentWord : myWords.entrySet()) {
					int theirValue = 0;
					if (otherPatent.getValue().get(myPatentWord.getKey()) != null) {
						theirValue = otherPatent.getValue().get(
								myPatentWord.getKey());
					}

					int frequency = 1;
					try {
						frequency = cpcDict.get(String.valueOf(first)).get(
								myPatentWord.getKey());

					} catch (Exception e) {
						// Twiddles thumbs...
					}

					sum += Math.pow((myPatentWord.getValue() - theirValue), 2)
							/ frequency;
				}
				correlation.put(otherPatent.getKey(), sum);
			}