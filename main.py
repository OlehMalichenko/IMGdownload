import os
import os

import requests

if __name__ == '__main__':
    # open file with image-links
    with open('files/ALL_IMPORT_MAIN.csv', 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)

        # create set with exist images
        if os.path.exists('files/added_img.csv'):
            check_set = set([row[0] for row in csv.reader(open('files/added_img.csv', 'r', encoding='utf-8'))])
        else:
            check_set = set()

        # open file for add parsed images
        with open('files/added_img.csv', 'a', encoding='utf-8', newline='\n') as fa:
            writer_added = csv.writer(fa)

            # open file for add rows with failed parsing
            with open('files/failed_rows.csv', 'a', encoding='utf-8', newline='\n') as f_failed:
                writer_failed = csv.DictWriter(f_failed, fieldnames=reader.fieldnames)
                writer_failed.writeheader()

                for row in reader:
                    sku = row['sku']

                    if sku in check_set:
                        continue

                    link_img = row['img']

                    try:
                        # get img from link
                        p = requests.get(link_img)

                        # write img
                        out = open(f'D:\\IMG\\{sku}.jpg', 'wb')
                        out.write(p.content)
                        out.close()

                        # add sku to check set and
                        check_set.add(sku)
                        writer_added.writerow([sku])
                        print(sku)
                    except:
                        print(f'======================FAILED ROW==={sku}')
                        writer_failed.writerow(row)
