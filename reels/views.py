# from django.shortcuts import render

# # Create your views here.




# import cloudinary.api

# def get_videos_from_folder(folder_name):
#     resources = cloudinary.api.resources(
#         type="upload",
#         prefix=folder_name + "/",
#         resource_type="video",
#         max_results=50
#     )
#     video_urls = [res['secure_url'] for res in resources['resources']]
#     print(video_urls)
#     return video_urls





# def show_reels(request):
#     video_urls = get_videos_from_folder("reels")
#     return render(request,'reels/show_reels.html',{'video_urls': video_urls})





# from django.shortcuts import render
# import cloudinary.api
# from cloudinary.exceptions import Error

# def get_videos_from_folder(folder_name):
#     try:
#         response = cloudinary.api.resources(
#             type="upload",
#             prefix=f"{folder_name}/",   # Example: "reels/"
#             resource_type="video",
#             max_results=50
#         )
#         video_urls = [res['secure_url'] for res in response['resources']]
#         print(video_urls)
#         return video_urls
#     except Error as e:
#         print("Cloudinary error:", e)
#         return []

# def show_reels(request):
#     video_urls = get_videos_from_folder("")  # Replace with your actual folder name
#     return render(request, 'reels/show_reels.html', {'video_urls': video_urls})





# from django.shortcuts import render
# import cloudinary.api
# from cloudinary.exceptions import Error

# def get_videos_from_folder(folder_name):
#     try:
#         response = cloudinary.api.resources(
#             type="upload",
#             prefix=f"{folder_name}/" if folder_name else "",  # Safe check
#             resource_type="video",
#             max_results=50
#         )
#         print("Cloudinary raw response:", response)  # Debug print
#         video_urls = [res['secure_url'] for res in response['resources']]
#         return video_urls
#     except Error as e:
#         print("Cloudinary error:", e)
#         return []

# def show_reels(request):
#     video_urls = get_videos_from_folder("")  # Empty if videos are in root
#     return render(request, 'reels/show_reels.html', {'video_urls': video_urls})




from django.shortcuts import render
import cloudinary.api
from cloudinary.exceptions import Error

def get_videos_from_folder(folder_name):
    try:
        # Step 1: Fetch all uploaded videos (up to 100)
        response = cloudinary.api.resources(
            type="upload",
            resource_type="video",
            max_results=100
        )
        
        # Step 2: Filter only those that match the folder
        filtered_resources = [
            res['secure_url'] 
            for res in response['resources'] 
            if res.get('asset_folder') == folder_name
        ]

        return filtered_resources

    except Error as e:
        print("Cloudinary error:", e)
        return []

def show_reels(request):
    video_urls = get_videos_from_folder("reels")
    return render(request, 'reels/show_reels.html', {'video_urls': video_urls})


