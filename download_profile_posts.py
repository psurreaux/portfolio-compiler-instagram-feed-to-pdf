import instaloader

ig = instaloader.Instaloader()

userId = 'surreartz'

# Download the profile
# Function to filter posts with images
def filter_images(post):
    return not post.is_video  

# Download only posts with images
ig.download_profile(userId, profile_pic_only=False, post_filter=filter_images)