from src.user.models import User


def get_or_create_user_through_github(github_profile: dict) -> User:

    user: User or None = User.query.filter_by(
        github_id=str(github_profile['id']),
    ).first()

    if user is not None:
        return user

    if 'email' in github_profile:
        user: User or None = User.query.filter_by(
            email=str(github_profile['email']),
        ).first()

        if user is not None:
            return user.update({
                'github_id': github_profile['id'],
                'is_oauth': True,
            })

    return User(
        login=github_profile['login'],
        email=github_profile['email'],
        firstname=github_profile['name'],
        github_id=github_profile['id'],
        image=github_profile['email'],
        is_oauth=False,
        is_aproved=True,
    ).save()
