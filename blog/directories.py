import time


def post_directory(instance, filename):
    return "/".join(
        ["images", "posts", f"{str(time.time())}_{instance.slug}_{str(filename)}"]
    )
