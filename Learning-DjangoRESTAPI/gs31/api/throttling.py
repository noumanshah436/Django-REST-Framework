from rest_framework.throttling import UserRateThrottle


class JackrateThrottle(UserRateThrottle):
    scope = "jack"


# here we are inheriting UserRateThrottle class, so that we can define the throttling rate separately fot the specific class