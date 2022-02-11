"""
    I/O operations for camera
"""
import cv2


def open_camera(camera=None):
    """
    open a specified camera webcam or URI

    :param camera: path or id of camera to be opened
    :return: boolean, frame
    :rtype: tuple
    """
    if camera is None:
        camera = 0  # opens webcam

    return cv2.VideoCapture(camera).read()  # returns if theres an output and the frame


def draw_rectangle(frame, pt1, pt2, color, thickness):
    """
    draw rectangle on image

    :param frame: camera output
    :type frame: bytearray
    :param pt1: rect coordinates
    :type pt1: tuple
    :param pt2: rect coordinates
    :type pt2: tuple
    :param color: rect color
    :type color: tuple
    :param thickness: boldness of rect outline
    :type thickness: int
    :rtype: None
    """
    if color is None:
        color = (0, 0, 255)

    if thickness is None:
        thickness = 2

    cv2.rectangle(
        frame,
        pt1,
        pt2,
        color,
        thickness
    )  # draws rect


def write_frames(filepath, frame):
    """
    saves images to file

    :param filepath: path + filename to save images
    :type filepath: str
    :param frame: image to save
    :type frame: bytearray
    :rtype: None
    """
    assert filepath is not None
    assert frame is not None

    cv2.imwrite(filepath, frame)  # saves frame to file

