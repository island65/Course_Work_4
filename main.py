from src.user_interaction import UserInteractionHH, UserInteractionJson


if __name__ == '__main__':
    user_hh_search = UserInteractionHH()
    user_hh_search.hh_user_search()

    user_json_search = UserInteractionJson()
    user_json_search.json_user_search()
