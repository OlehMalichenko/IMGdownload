import csv

if __name__ == '__main__':

	with open('files/ALL_IMPORT_MAIN_dropdublicates.csv', 'r', encoding='utf-8') as f:
		reader = csv.DictReader(f)
		fielnames_before = reader.fieldnames
		fieldnames = list(fielnames_before) + ['actual_price']

		with open('files/ALL_IMPORT_MAIN_dropdublicates_actualprice.csv', 'a', encoding='utf-8', newline='\n') as fd:
			writer = csv.DictWriter(fd, fieldnames=fieldnames)
			writer.writeheader()

			with open('files/ALL_IMPORT_MAIN_failedprice.csv', 'a', encoding='utf-8', newline='\n') as ffp:
				writer_ffp = csv.DictWriter(ffp, fieldnames=fielnames_before)
				writer_ffp.writeheader()

				for row in reader:
					try:
						price = float(str(row['price']).strip())
						if not price:
							writer_ffp.writerow(row)
							continue
					except:
						writer_ffp.writerow(row)
						continue
					else:
						sale = str(row['sale_price']).strip()
						if sale and sale != '0.0' and sale != '0':
							try:
								actual_price = float(sale)
							except:
								writer_ffp.writerow(row)
								continue
						else:
							actual_price = price

						row['actual_price'] = actual_price
						writer.writerow(row)
