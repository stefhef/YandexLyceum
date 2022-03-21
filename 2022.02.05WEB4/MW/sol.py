import argparse
import os


def format_text_block(frame_height, frame_width, file_name):
    try:
        os.path.exists(file_name)
        st: str = ''
        ls_st = []
        with open(file_name, encoding='utf-8') as file:
            data = list(map(str.strip, file.readlines()))
        for elem in data:
            if not elem:
                if st:
                    ls_st.append(st)
                    st = ''
                ls_st.append(elem)
            for el in elem:
                st += el
                if len(st) == frame_width or not el:
                    ls_st.append(st)
                    if len(ls_st) == frame_height:
                        break
                    st = ''

        return "\n".join(ls_st[:frame_height])
    except BaseException as e:
        return e


if __name__ == '__main__':
    params = argparse.ArgumentParser()
    params.add_argument('--frame-height', default=0, nargs=1, type=int)
    params.add_argument('--frame-width', default=0, nargs=1, type=int)
    params.add_argument('file_name', default='', nargs=1)
    arg = params.parse_args()
    print(format_text_block(arg.frame_height[0], arg.frame_width[0], arg.file_name[0]))
