#필요한 모듈 'parking_spot_manager', 'file_manager' 추가
import parking_spot_manager
import file_manager

def start_process(path):
    #주소 path의 텍스트 파일 읽고, 한 줄씩 리스트에 저장
    str_list = file_manager.read_file(path)
    #한 줄의 정보를 담을 리스트 선언
    place = []
    length = len(str_list)

    #한 줄마다 쉼표로 구분해 정보 저장, 저장한 정보로 parking_spot 객체 생성, 리스트 place에 객체 삽입
    for i in range(length):
        info = str_list[i].split(',')
        temp_place = parking_spot_manager.parking_spot(info[1], info[2], info[3], info[4], info[5], info[6])
        place.append(temp_place)
    while True:
        print("---menu---")
        print("[1] print")
        print("[2] filter")
        print("[3] sort")
        print("[4] exit")
        select = int(input('type:'))
        if select == 1:
            #저장된 리스트 place 출력
            parking_spot_manager.print_spots(place)
        elif select == 2:
            print("---filter by---")
            print("[1] name")
            print("[2] city")
            print("[3] district")
            print("[4] ptype")
            print("[5] location")
            select = int(input('type:'))
            if select == 1:
                keyword = input('type name:')
                place = parking_spot_manager.filter_by_name(place, keyword)     #주차장 이름 필터링
            elif select == 2:
                keyword = input('type city:')           
                place = parking_spot_manager.filter_by_city(place, keyword)     #도시 이름 필터링
            elif select == 3:
                keyword = input('type district:')
                place = parking_spot_manager.filter_by_district(place, keyword)     #지역 필터링
            elif select == 4:
                keyword = input('type ptype:')
                place = parking_spot_manager.filter_by_ptype(place, keyword)        #주차장 유형 필터링
            elif select == 5:
                #위도 경도 최대 최소 입력
                min_lat = float(input('type min lat:'))
                max_lat = float(input('type max lat:'))
                min_lon = float(input('type min long:'))
                max_lon = float(input('type max long:'))
                # 위치(위도, 경도) 필터링
                place = parking_spot_manager.filter_by_location(place, (min_lat, max_lat, min_lon, max_lon))
            else:
                print("invalid input")
        elif select == 3:
            keywords = ['name', 'city', 'district', 'ptype', 'latitude', 'longitude']
            print("---sort by---")
            print(keywords)
            keyword = input('type keyword:')
            if keyword in keywords:
                print("not implemented yet")
                # fill this block
            else: print("invalid input")
        elif select == 4:
            print("Exit")
            break
        else:
            print("invalid input")