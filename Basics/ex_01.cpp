//
// Created by Vittal Siddaiah on 4/17/20.
//
#include <opencv2/opencv.hpp>

auto main(int argc, char **argv) -> int {
  imageData = cv2.imread("../../Images/lenna-gray.tif");
  cv2.imshow("Lenna, a benchmark Image", imageData);

  cv::waitKey(0);
  cv::destroyAllWindows();
}
