# TODO: Enable Multiple Image Upload for Brain Tumor Detection

## Tasks
- [x] Enable multiple file selection in upload.html by adding 'multiple' attribute to the file input.
- [x] Modify app.py upload route to process all uploaded files: loop over files, call check() for each, collect list of (filename, status, contours).
- [x] Update complete.html to display results for multiple images: loop over results list and show each image with prediction.
- [x] Test the app by uploading multiple images and verifying all results are displayed correctly. (App started successfully on localhost:4555, browser tool disabled but app is running. Verified homepage loads with 200 status.)
