## Image to Text ~ [GHW 2023(FEB)](https://ghw.mlh.io)
> [Demo Video](https://youtu.be/w9qiQ4FPzEw)

A simple python project which uses `tesseract` and `openCV` library to achieve a simple Image to Text Script.

## Execution Path

1. Get Images List from `./images` folder.
2. Iterate over the `images` list.
3. For every image, get image `matrix` using `openCV` library.
4. Using `tesseract` library get text from the `matrix` obtained.
5. Append the output obtained in `output.txt` file.
