class parking_spot:
    # you have to implement 'constructor(생성자)' and 'get' method

    # __init__ 생성자를 사용하여 item 딕셔너리를 생성 
    # 클래스 객체 선언 시, item 딕셔너리의 값을 결정한다.
    def __init__(self, name, city, district, ptype, longitude, latitude):
        self.__item = {'name':' ', 'city':' ', 'district':' ', 'ptype':' ', 'longitude':0.0, 'latitude':0.0}
        self.__item['name'] = str(name)
        self.__item['city'] = str(city)
        self.__item['district'] = str(district)
        self.__item['ptype'] = str(ptype)
        self.__item['longitude'] = float(longitude)
        self.__item['latitude'] = float(latitude)

    # get 메소드: class parking_spot 객체의 keyword 값 반환
    def get(self, keyword='name'):
        return self.__item[keyword]
    
    def __str__(self):
        item = self.__item
        s  = f"[{item['name']}({item['ptype']})] "
        s += f"{item['city']} {item['district']}"
        s += f"(lat:{item['latitude']}, long:{item['longitude']})"
        return s

def str_list_to_class_list(str_list):
    #한 줄의 정보를 담을 리스트 선언
    place = []
    length = len(str_list)     
    
    for i in range(length):
        #한 줄마다 쉼표로 구분해 정보 저장, 저장한 정보로 parking_spot 객체 생성, 리스트 place에 객체 삽입
        info = str_list[i].split(',')
        temp_place = parking_spot(info[1], info[2], info[3], info[4], info[5], info[6])
        place.append(temp_place)
    
    return place
    
def print_spots(spots):
    length = len(spots)
    print(f"---print elements({length})---")
    # 한 줄마다 정보 출력
    for i in spots:
        print(i)

def filter_by_name(spots, name):
    # 포함된 이름 필터링
    new_list = [i for i in spots if name in i.get('name')]
    return new_list

def filter_by_city(spots, city):
    # 도시 이름 필터링
    new_list = [i for i in spots if city in i.get('city')]
    return new_list

def filter_by_district(spots, district):
    # 지역 필터링
    new_list = [i for i in spots if district in i.get('district')]
    return new_list

def filter_by_ptype(spots, ptype):
    # 주차장 유형 필터링
    new_list = [i for i in spots if ptype in i.get('ptype')]
    return new_list

def filter_by_location(spots, locations):
    #최대 최소 위도 경도 설정
    min_lat = locations[0]
    max_lat = locations[1]
    min_lon = locations[2]
    max_lon = locations[3]
    # 위치(위도, 경도) 필터링
    new_list = [i for i in spots if (min_lat < i.get('latitude') < max_lat and min_lon < i.get('longitude') < max_lon)]
    return new_list

def sort_by_keyword(spots, keyword):
    #입력 받은 항목으로 오름차순 정렬
    new_list = sorted(spots, key=lambda x : x.get(keyword))
    return new_list

# 각 단계별로 테스트 (테스트할때 주석해제 후 사용)
if __name__ == '__main__':
    print("Testing the module...")
    # version#2
    # import file_manager
    # str_list = file_manager.read_file("./input/free_parking_spot_seoul.csv")
    # spots = str_list_to_class_list(str_list)
    # sprint_spots(spots)

    # version#3
    # spots = filter_by_district(spots, '동작')
    # print_spots(spots)
    
    # version#4
    # spots = sort_by_keyword(spots, 'name')
    # print_spots(spots)