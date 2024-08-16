def get_flat_images_path(flat_obj, filename):
    return f'flats_images/{flat_obj.id}/{filename}'

def get_user_avatar_path(user_obj):
    return f'users_avatars/{user_obj.username}'