from rabbit_mq_producer import publish_event_rmq
message = """{
        "username" : "shuvendu",
        "event_group_name" : "USER",
        "event_type" : "Login",
        "event_info" : {
            "message" : "User shuvendu logged in successfully.",
            "username" : "shuvendu"
        },
        "timestamp" : NumberLong(1619604834338)
    }"""
print("Sending Message : ")
publish_event_rmq(message,'test.info.test1')
