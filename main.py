from bing_image_downloader import downloader
query_string = "Single Golf Stick images"
downloader.download(query_string, limit=100,  output_dir='dataset', 
adult_filter_off=True, force_replace=False, timeout=60)
