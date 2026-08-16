# 프롬프트 관리 프로그램

# 기본 데이터
prompts = [
    {
        "title": "블로그 글 작성 도우미",
        "content": "당신은 10년 경력의 전문 블로거입니다. 주어진 주제에 대해 SEO에 최적화된 블로그 글을 작성해주세요.",
        "category": "텍스트 생성",
        "favorite": False
    },
    {
        "title": "제품 썸네일 생성",
        "content": "다음 제품의 매력적인 썸네일 이미지를 생성해주세요. 배경은 흰색, 제품이 중앙에 위치하도록 해주세요.",
        "category": "이미지 생성",
        "favorite": False
    },
    {
        "title": "IT 컨설턴트 페르소나",
        "content": "당신은 15년 경력의 IT 컨설턴트입니다. 기업의 디지털 전환 전략을 수립하는 전문가로서 답변해주세요.",
        "category": "페르소나",
        "favorite": False
    }
]

# 카테고리 목록
categories = ["텍스트 생성", "이미지 생성", "영상 생성", "페르소나", "자동화", "기타"]
# 기본 프롬프트 데이터 (이전 미션에서 작성)
prompts = [
    {
        "title": "회의록 요약 시스템 프롬프트",
        "content": "너는 회의록 요약 전문가다. 원문을 기반으로 핵심 논의사항, 결정사항, 액션아이템을 구조화하여 요약하는 것이 목표다. [답변 형식] 핵심 논의사항(bullet) / 결정사항(bullet) / 액션아이템(담당자-할일-기한 표) / 확인 필요 항목을 고정 구조로 사용한다. [안전장치] 원문에 없는 숫자·날짜·이름은 절대 생성하지 않으며, 불명확한 내용은 (확인 필요)로 표기한다.",
        "category": "텍스트 생성",
        "favorite": False
    },
    {
        "title": "FreshKeeper UI 디자인 이미지 생성",
        "content": "자취생용 냉장고 식재료 리마인더 앱 'FreshKeeper'의 모바일 UI 화면을 생성해줘. 화면 비율은 390x844px 세로형. 디자인 키워드는 Clean, Fresh, Friendly, Minimal, Mobile First. 동일한 컬러·타이포·카드 모서리·하단 내비게이션을 유지하고, 화면 잘림 금지, 임의 기능 추가 금지 조건을 지켜줘.",
        "category": "이미지 생성",
        "favorite": False
    },
    {
        "title": "구글시트 응답 자동 이메일 발송",
        "content": "구글폼 응답이 구글시트에 저장되면 새 행을 감지해서, 제출된 영상 길이(G열)가 10초 이하면 '접수 완료' 안내 메일을, 10초를 초과하면 '길이 초과, 재제출 요청' 안내 메일을 제출자 이메일(H열)로 자동 발송하는 Make.com 자동화 워크플로우를 만들어줘.",
        "category": "자동화",
        "favorite": False
    },
]



# 메뉴 출력 함수
def show_menu():
    print("\n=== 나만의 프롬프트 관리 ===")
    print("1. 프롬프트 추가")
    print("2. 프롬프트 목록")
    print("3. 카테고리별 조회")
    print("4. 프롬프트 검색")
    print("5. 프롬프트 상세 보기")
    print("6. 즐겨찾기 관리")
    print("7. 즐겨찾기 목록")
    print("0. 종료")


# 메인 실행
def main():
    while True:
        show_menu()
        choice = input("선택: ")

        if choice == "0":
            print("프로그램을 종료합니다.")
            break
        else:
            print("아직 준비 중인 기능입니다.")


main()
