from tkinter import *
from tkinter.messagebox import *

window = Tk()
window.geometry("300x300")
window.title("mon app fenetre ")
window.mainloop()



    creating build/lib.macosx-10.9-x86_64-3.8/pygame/tests/run_tests__tests/everything
    copying test/run_tests__tests/everything/sleep_test.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/tests/run_tests__tests/everything
    copying test/run_tests__tests/everything/magic_tag_test.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/tests/run_tests__tests/everything
    copying test/run_tests__tests/everything/fake_2_test.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/tests/run_tests__tests/everything
    copying test/run_tests__tests/everything/incomplete_todo_test.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/tests/run_tests__tests/everything
    copying test/run_tests__tests/everything/__init__.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/tests/run_tests__tests/everything
    creating build/lib.macosx-10.9-x86_64-3.8/pygame/docs
    copying docs/__init__.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/docs
    copying docs/__main__.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/docs
    creating build/lib.macosx-10.9-x86_64-3.8/pygame/examples
    copying examples/playmus.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/examples
    copying examples/mask.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/examples
    copying examples/sound.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/examples
    copying examples/overlay.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/examples
    copying examples/aacircle.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/examples
    copying examples/chimp.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/examples
    copying examples/liquid.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/examples
    copying examples/audiocapture.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/examples
    copying examples/sound_array_demos.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/examples
    copying examples/midi.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/examples
    copying examples/scroll.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/examples
    copying examples/cursors.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/examples
    copying examples/moveit.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/examples
    copying examples/__init__.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/examples
    copying examples/blit_blends.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/examples
    copying examples/testsprite.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/examples
    copying examples/textinput.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/examples
    copying examples/vgrade.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/examples
    copying examples/arraydemo.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/examples
    copying examples/stars.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/examples
    copying examples/camera.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/examples
    copying examples/blend_fill.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/examples
    copying examples/fonty.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/examples
    copying examples/headless_no_windows_needed.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/examples
    copying examples/fastevents.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/examples
    copying examples/prevent_display_stretching.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/examples
    copying examples/glcube.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/examples
    copying examples/aliens.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/examples
    copying examples/freetype_misc.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/examples
    copying examples/scaletest.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/examples
    copying examples/video.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/examples
    copying examples/eventlist.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/examples
    copying examples/scrap_clipboard.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/examples
    copying examples/oldalien.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/examples
    copying examples/pixelarray.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/examples
    copying examples/dropevent.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/examples
    running build_ext
    building 'pygame.gfxdraw' extension
    creating build/temp.macosx-10.9-x86_64-3.8
    creating build/temp.macosx-10.9-x86_64-3.8/src_c
    creating build/temp.macosx-10.9-x86_64-3.8/src_c/SDL_gfx
    gcc -Wno-unused-result -Wsign-compare -Wunreachable-code -fno-common -dynamic -DNDEBUG -g -fwrapv -O3 -Wall -arch x86_64 -g -DENABLE_NEWBUF=1 -I/NEED_INC_PATH_FIX -I/Library/Frameworks/Python.framework/Versions/3.8/include/python3.8 -c src_c/gfxdraw.c -o build/temp.macosx-10.9-x86_64-3.8/src_c/gfxdraw.o
    In file included from src_c/gfxdraw.c:33:
    In file included from src_c/pygame.h:32:
    src_c/_pygame.h:216:10: fatal error: 'SDL.h' file not found
    #include <SDL.h>
             ^~~~~~~
    1 error generated.
    ---
    For help with compilation see:
        https://www.pygame.org/wiki/MacCompile
    To contribute to pygame development see:
        https://www.pygame.org/contribute.html
    ---
    error: command 'gcc' failed with exit status 1
    ----------------------------------------
ERROR: Command errored out with exit status 1: /usr/local/bin/python3.8 -u -c 'import sys, setuptools, tokenize; sys.argv[0] = '"'"'/private/var/folders/_7/5n355t_90h1_313mp_ly99kc0000gn/T/pip-install-elja7qrx/pygame/setup.py'"'"'; __file__='"'"'/private/var/folders/_7/5n355t_90h1_313mp_ly99kc0000gn/T/pip-install-elja7qrx/pygame/setup.py'"'"';f=getattr(tokenize, '"'"'open'"'"', open)(__file__);code=f.read().replace('"'"'\r\n'"'"', '"'"'\n'"'"');f.close();exec(compile(code, __file__, '"'"'exec'"'"'))' install --record /private/var/folders/_7/5n355t_90h1_313mp_ly99kc0000gn/T/pip-record-0f9y52e_/install-record.txt --single-version-externally-managed --compile --install-headers /Library/Frameworks/Python.framework/Versions/3.8/include/python3.8/pygame Check the logs for full command output.
MacBook-Pro-de-Spart:tp7 spart$ pip install wheel
Requirement already satisfied: wheel in /Library/Frameworks/Python.framework/Versions/3.8/lib/python3.8/site-packages (0.34.2)
MacBook-Pro-de-Spart:tp7 spart$ pip3 install pygame
Collecting pygame
  Using cached pygame-1.9.6.tar.gz (3.2 MB)
Building wheels for collected packages: pygame
  Building wheel for pygame (setup.py) ... error
  ERROR: Command errored out with exit status 1:
   command: /usr/local/bin/python3.8 -u -c 'import sys, setuptools, tokenize; sys.argv[0] = '"'"'/private/var/folders/_7/5n355t_90h1_313mp_ly99kc0000gn/T/pip-install-lm1nshs4/pygame/setup.py'"'"'; __file__='"'"'/private/var/folders/_7/5n355t_90h1_313mp_ly99kc0000gn/T/pip-install-lm1nshs4/pygame/setup.py'"'"';f=getattr(tokenize, '"'"'open'"'"', open)(__file__);code=f.read().replace('"'"'\r\n'"'"', '"'"'\n'"'"');f.close();exec(compile(code, __file__, '"'"'exec'"'"'))' bdist_wheel -d /private/var/folders/_7/5n355t_90h1_313mp_ly99kc0000gn/T/pip-wheel-g06xb7nk
       cwd: /private/var/folders/_7/5n355t_90h1_313mp_ly99kc0000gn/T/pip-install-lm1nshs4/pygame/
  Complete output (218 lines):
  running bdist_wheel
  running build
  running build_py
  creating build
  creating build/lib.macosx-10.9-x86_64-3.8
  creating build/lib.macosx-10.9-x86_64-3.8/pygame
  copying src_py/surfarray.py -> build/lib.macosx-10.9-x86_64-3.8/pygame
  copying src_py/sysfont.py -> build/lib.macosx-10.9-x86_64-3.8/pygame
  copying src_py/_camera_vidcapture.py -> build/lib.macosx-10.9-x86_64-3.8/pygame
  copying src_py/sndarray.py -> build/lib.macosx-10.9-x86_64-3.8/pygame
  copying src_py/version.py -> build/lib.macosx-10.9-x86_64-3.8/pygame
  copying src_py/compat.py -> build/lib.macosx-10.9-x86_64-3.8/pygame
  copying src_py/draw_py.py -> build/lib.macosx-10.9-x86_64-3.8/pygame
  copying src_py/colordict.py -> build/lib.macosx-10.9-x86_64-3.8/pygame
  copying src_py/ftfont.py -> build/lib.macosx-10.9-x86_64-3.8/pygame
  copying src_py/midi.py -> build/lib.macosx-10.9-x86_64-3.8/pygame
  copying src_py/cursors.py -> build/lib.macosx-10.9-x86_64-3.8/pygame
  copying src_py/__init__.py -> build/lib.macosx-10.9-x86_64-3.8/pygame
  copying src_py/_numpysndarray.py -> build/lib.macosx-10.9-x86_64-3.8/pygame
  copying src_py/sprite.py -> build/lib.macosx-10.9-x86_64-3.8/pygame
  copying src_py/macosx.py -> build/lib.macosx-10.9-x86_64-3.8/pygame
  copying src_py/_numpysurfarray.py -> build/lib.macosx-10.9-x86_64-3.8/pygame
  copying src_py/camera.py -> build/lib.macosx-10.9-x86_64-3.8/pygame
  copying src_py/freetype.py -> build/lib.macosx-10.9-x86_64-3.8/pygame
  copying src_py/_camera_opencv_highgui.py -> build/lib.macosx-10.9-x86_64-3.8/pygame
  copying src_py/pkgdata.py -> build/lib.macosx-10.9-x86_64-3.8/pygame
  copying src_py/locals.py -> build/lib.macosx-10.9-x86_64-3.8/pygame
  copying src_py/_dummybackend.py -> build/lib.macosx-10.9-x86_64-3.8/pygame
  creating build/lib.macosx-10.9-x86_64-3.8/pygame/threads
  copying src_py/threads/Py25Queue.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/threads
  copying src_py/threads/__init__.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/threads
  creating build/lib.macosx-10.9-x86_64-3.8/pygame/tests
  copying test/base_test.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/tests
  copying test/font_test.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/tests
  copying test/mixer_test.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/tests
  copying test/rwobject_test.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/tests
  copying test/pixelcopy_test.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/tests
  copying test/overlay_test.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/tests
  copying test/scrap_test.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/tests
  copying test/touch_tags.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/tests
  copying test/imageext_tags.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/tests
  copying test/pixelarray_test.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/tests
  copying test/draw_test.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/tests
  copying test/transform_test.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/tests
  copying test/blit_test.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/tests
  copying test/bufferproxy_test.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/tests
  copying test/surfarray_test.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/tests
  copying test/mouse_test.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/tests
  copying test/surfarray_tags.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/tests
  copying test/event_test.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/tests
  copying test/imageext_test.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/tests
  copying test/sprite_test.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/tests
  copying test/touch_test.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/tests
  copying test/gfxdraw_test.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/tests
  copying test/rect_test.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/tests
  copying test/scrap_tags.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/tests
  copying test/__init__.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/tests
  copying test/overlay_tags.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/tests
  copying test/color_test.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/tests
  copying test/camera_test.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/tests
  copying test/surflock_test.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/tests
  copying test/key_test.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/tests
  copying test/sysfont_test.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/tests
  copying test/font_tags.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/tests
  copying test/mixer_tags.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/tests
  copying test/constants_test.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/tests
  copying test/mixer_music_tags.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/tests
  copying test/sndarray_test.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/tests
  copying test/image_test.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/tests
  copying test/version_test.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/tests
  copying test/freetype_test.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/tests
  copying test/joystick_test.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/tests
  copying test/midi_tags.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/tests
  copying test/ftfont_tags.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/tests
  copying test/image__save_gl_surface_test.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/tests
  copying test/cdrom_tags.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/tests
  copying test/cursors_test.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/tests
  copying test/fastevent_tags.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/tests
  copying test/display_test.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/tests
  copying test/fastevent_test.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/tests
  copying test/compat_test.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/tests
  copying test/ftfont_test.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/tests
  copying test/cdrom_test.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/tests
  copying test/mask_test.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/tests
  copying test/midi_test.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/tests
  copying test/freetype_tags.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/tests
  copying test/math_test.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/tests
  copying test/time_test.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/tests
  copying test/image_tags.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/tests
  copying test/threads_test.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/tests
  copying test/__main__.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/tests
  copying test/mixer_music_test.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/tests
  copying test/sndarray_tags.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/tests
  copying test/test_test_.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/tests
  copying test/surface_test.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/tests
  creating build/lib.macosx-10.9-x86_64-3.8/pygame/tests/test_utils
  copying test/test_utils/run_tests.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/tests/test_utils
  copying test/test_utils/endian.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/tests/test_utils
  copying test/test_utils/test_machinery.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/tests/test_utils
  copying test/test_utils/__init__.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/tests/test_utils
  copying test/test_utils/png.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/tests/test_utils
  copying test/test_utils/test_runner.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/tests/test_utils
  copying test/test_utils/arrinter.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/tests/test_utils
  copying test/test_utils/buftools.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/tests/test_utils
  copying test/test_utils/async_sub.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/tests/test_utils
  creating build/lib.macosx-10.9-x86_64-3.8/pygame/tests/run_tests__tests
  copying test/run_tests__tests/run_tests__test.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/tests/run_tests__tests
  copying test/run_tests__tests/__init__.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/tests/run_tests__tests
  creating build/lib.macosx-10.9-x86_64-3.8/pygame/tests/run_tests__tests/all_ok
  copying test/run_tests__tests/all_ok/fake_3_test.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/tests/run_tests__tests/all_ok
  copying test/run_tests__tests/all_ok/fake_2_test.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/tests/run_tests__tests/all_ok
  copying test/run_tests__tests/all_ok/__init__.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/tests/run_tests__tests/all_ok
  copying test/run_tests__tests/all_ok/fake_4_test.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/tests/run_tests__tests/all_ok
  copying test/run_tests__tests/all_ok/fake_5_test.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/tests/run_tests__tests/all_ok
  copying test/run_tests__tests/all_ok/no_assertions__ret_code_of_1__test.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/tests/run_tests__tests/all_ok
  copying test/run_tests__tests/all_ok/zero_tests_test.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/tests/run_tests__tests/all_ok
  copying test/run_tests__tests/all_ok/fake_6_test.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/tests/run_tests__tests/all_ok
  creating build/lib.macosx-10.9-x86_64-3.8/pygame/tests/run_tests__tests/failures1
  copying test/run_tests__tests/failures1/fake_3_test.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/tests/run_tests__tests/failures1
  copying test/run_tests__tests/failures1/fake_2_test.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/tests/run_tests__tests/failures1
  copying test/run_tests__tests/failures1/__init__.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/tests/run_tests__tests/failures1
  copying test/run_tests__tests/failures1/fake_4_test.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/tests/run_tests__tests/failures1
  creating build/lib.macosx-10.9-x86_64-3.8/pygame/tests/run_tests__tests/incomplete
  copying test/run_tests__tests/incomplete/fake_3_test.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/tests/run_tests__tests/incomplete
  copying test/run_tests__tests/incomplete/fake_2_test.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/tests/run_tests__tests/incomplete
  copying test/run_tests__tests/incomplete/__init__.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/tests/run_tests__tests/incomplete
  creating build/lib.macosx-10.9-x86_64-3.8/pygame/tests/run_tests__tests/infinite_loop
  copying test/run_tests__tests/infinite_loop/fake_2_test.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/tests/run_tests__tests/infinite_loop
  copying test/run_tests__tests/infinite_loop/fake_1_test.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/tests/run_tests__tests/infinite_loop
  copying test/run_tests__tests/infinite_loop/__init__.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/tests/run_tests__tests/infinite_loop
  creating build/lib.macosx-10.9-x86_64-3.8/pygame/tests/run_tests__tests/print_stderr
  copying test/run_tests__tests/print_stderr/fake_3_test.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/tests/run_tests__tests/print_stderr
  copying test/run_tests__tests/print_stderr/fake_2_test.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/tests/run_tests__tests/print_stderr
  copying test/run_tests__tests/print_stderr/__init__.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/tests/run_tests__tests/print_stderr
  copying test/run_tests__tests/print_stderr/fake_4_test.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/tests/run_tests__tests/print_stderr
  creating build/lib.macosx-10.9-x86_64-3.8/pygame/tests/run_tests__tests/print_stdout
  copying test/run_tests__tests/print_stdout/fake_3_test.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/tests/run_tests__tests/print_stdout
  copying test/run_tests__tests/print_stdout/fake_2_test.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/tests/run_tests__tests/print_stdout
  copying test/run_tests__tests/print_stdout/__init__.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/tests/run_tests__tests/print_stdout
  copying test/run_tests__tests/print_stdout/fake_4_test.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/tests/run_tests__tests/print_stdout
  creating build/lib.macosx-10.9-x86_64-3.8/pygame/tests/run_tests__tests/incomplete_todo
  copying test/run_tests__tests/incomplete_todo/fake_3_test.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/tests/run_tests__tests/incomplete_todo
  copying test/run_tests__tests/incomplete_todo/fake_2_test.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/tests/run_tests__tests/incomplete_todo
  copying test/run_tests__tests/incomplete_todo/__init__.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/tests/run_tests__tests/incomplete_todo
  creating build/lib.macosx-10.9-x86_64-3.8/pygame/tests/run_tests__tests/exclude
  copying test/run_tests__tests/exclude/magic_tag_test.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/tests/run_tests__tests/exclude
  copying test/run_tests__tests/exclude/fake_2_test.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/tests/run_tests__tests/exclude
  copying test/run_tests__tests/exclude/__init__.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/tests/run_tests__tests/exclude
  copying test/run_tests__tests/exclude/invisible_tag_test.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/tests/run_tests__tests/exclude
  creating build/lib.macosx-10.9-x86_64-3.8/pygame/tests/run_tests__tests/timeout
  copying test/run_tests__tests/timeout/sleep_test.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/tests/run_tests__tests/timeout
  copying test/run_tests__tests/timeout/fake_2_test.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/tests/run_tests__tests/timeout
  copying test/run_tests__tests/timeout/__init__.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/tests/run_tests__tests/timeout
  creating build/lib.macosx-10.9-x86_64-3.8/pygame/tests/run_tests__tests/everything
  copying test/run_tests__tests/everything/sleep_test.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/tests/run_tests__tests/everything
  copying test/run_tests__tests/everything/magic_tag_test.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/tests/run_tests__tests/everything
  copying test/run_tests__tests/everything/fake_2_test.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/tests/run_tests__tests/everything
  copying test/run_tests__tests/everything/incomplete_todo_test.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/tests/run_tests__tests/everything
  copying test/run_tests__tests/everything/__init__.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/tests/run_tests__tests/everything
  creating build/lib.macosx-10.9-x86_64-3.8/pygame/docs
  copying docs/__init__.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/docs
  copying docs/__main__.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/docs
  creating build/lib.macosx-10.9-x86_64-3.8/pygame/examples
  copying examples/playmus.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/examples
  copying examples/mask.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/examples
  copying examples/sound.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/examples
  copying examples/overlay.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/examples
  copying examples/aacircle.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/examples
  copying examples/chimp.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/examples
  copying examples/liquid.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/examples
  copying examples/audiocapture.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/examples
  copying examples/sound_array_demos.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/examples
  copying examples/midi.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/examples
  copying examples/scroll.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/examples
  copying examples/cursors.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/examples
  copying examples/moveit.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/examples
  copying examples/__init__.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/examples
  copying examples/blit_blends.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/examples
  copying examples/testsprite.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/examples
  copying examples/textinput.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/examples
  copying examples/vgrade.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/examples
  copying examples/arraydemo.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/examples
  copying examples/stars.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/examples
  copying examples/camera.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/examples
  copying examples/blend_fill.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/examples
  copying examples/fonty.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/examples
  copying examples/headless_no_windows_needed.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/examples
  copying examples/fastevents.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/examples
  copying examples/prevent_display_stretching.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/examples
  copying examples/glcube.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/examples
  copying examples/aliens.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/examples
  copying examples/freetype_misc.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/examples
  copying examples/scaletest.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/examples
  copying examples/video.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/examples
  copying examples/eventlist.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/examples
  copying examples/scrap_clipboard.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/examples
  copying examples/oldalien.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/examples
  copying examples/pixelarray.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/examples
  copying examples/dropevent.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/examples
  running build_ext
  building 'pygame.gfxdraw' extension
  creating build/temp.macosx-10.9-x86_64-3.8
  creating build/temp.macosx-10.9-x86_64-3.8/src_c
  creating build/temp.macosx-10.9-x86_64-3.8/src_c/SDL_gfx
  gcc -Wno-unused-result -Wsign-compare -Wunreachable-code -fno-common -dynamic -DNDEBUG -g -fwrapv -O3 -Wall -arch x86_64 -g -DENABLE_NEWBUF=1 -I/NEED_INC_PATH_FIX -I/Library/Frameworks/Python.framework/Versions/3.8/include/python3.8 -c src_c/gfxdraw.c -o build/temp.macosx-10.9-x86_64-3.8/src_c/gfxdraw.o
  In file included from src_c/gfxdraw.c:33:
  In file included from src_c/pygame.h:32:
  src_c/_pygame.h:216:10: fatal error: 'SDL.h' file not found
  #include <SDL.h>
           ^~~~~~~
  1 error generated.
  ---
  For help with compilation see:
      https://www.pygame.org/wiki/MacCompile
  To contribute to pygame development see:
      https://www.pygame.org/contribute.html
  ---
  error: command 'gcc' failed with exit status 1
  ----------------------------------------
  ERROR: Failed building wheel for pygame
  Running setup.py clean for pygame
Failed to build pygame
Installing collected packages: pygame
    Running setup.py install for pygame ... error
    ERROR: Command errored out with exit status 1:
     command: /usr/local/bin/python3.8 -u -c 'import sys, setuptools, tokenize; sys.argv[0] = '"'"'/private/var/folders/_7/5n355t_90h1_313mp_ly99kc0000gn/T/pip-install-lm1nshs4/pygame/setup.py'"'"'; __file__='"'"'/private/var/folders/_7/5n355t_90h1_313mp_ly99kc0000gn/T/pip-install-lm1nshs4/pygame/setup.py'"'"';f=getattr(tokenize, '"'"'open'"'"', open)(__file__);code=f.read().replace('"'"'\r\n'"'"', '"'"'\n'"'"');f.close();exec(compile(code, __file__, '"'"'exec'"'"'))' install --record /private/var/folders/_7/5n355t_90h1_313mp_ly99kc0000gn/T/pip-record-chq_za3o/install-record.txt --single-version-externally-managed --compile --install-headers /Library/Frameworks/Python.framework/Versions/3.8/include/python3.8/pygame
         cwd: /private/var/folders/_7/5n355t_90h1_313mp_ly99kc0000gn/T/pip-install-lm1nshs4/pygame/
    Complete output (218 lines):
    running install
    running build
    running build_py
    creating build
    creating build/lib.macosx-10.9-x86_64-3.8
    creating build/lib.macosx-10.9-x86_64-3.8/pygame
    copying src_py/surfarray.py -> build/lib.macosx-10.9-x86_64-3.8/pygame
    copying src_py/sysfont.py -> build/lib.macosx-10.9-x86_64-3.8/pygame
    copying src_py/_camera_vidcapture.py -> build/lib.macosx-10.9-x86_64-3.8/pygame
    copying src_py/sndarray.py -> build/lib.macosx-10.9-x86_64-3.8/pygame
    copying src_py/version.py -> build/lib.macosx-10.9-x86_64-3.8/pygame
    copying src_py/compat.py -> build/lib.macosx-10.9-x86_64-3.8/pygame
    copying src_py/draw_py.py -> build/lib.macosx-10.9-x86_64-3.8/pygame
    copying src_py/colordict.py -> build/lib.macosx-10.9-x86_64-3.8/pygame
    copying src_py/ftfont.py -> build/lib.macosx-10.9-x86_64-3.8/pygame
    copying src_py/midi.py -> build/lib.macosx-10.9-x86_64-3.8/pygame
    copying src_py/cursors.py -> build/lib.macosx-10.9-x86_64-3.8/pygame
    copying src_py/__init__.py -> build/lib.macosx-10.9-x86_64-3.8/pygame
    copying src_py/_numpysndarray.py -> build/lib.macosx-10.9-x86_64-3.8/pygame
    copying src_py/sprite.py -> build/lib.macosx-10.9-x86_64-3.8/pygame
    copying src_py/macosx.py -> build/lib.macosx-10.9-x86_64-3.8/pygame
    copying src_py/_numpysurfarray.py -> build/lib.macosx-10.9-x86_64-3.8/pygame
    copying src_py/camera.py -> build/lib.macosx-10.9-x86_64-3.8/pygame
    copying src_py/freetype.py -> build/lib.macosx-10.9-x86_64-3.8/pygame
    copying src_py/_camera_opencv_highgui.py -> build/lib.macosx-10.9-x86_64-3.8/pygame
    copying src_py/pkgdata.py -> build/lib.macosx-10.9-x86_64-3.8/pygame
    copying src_py/locals.py -> build/lib.macosx-10.9-x86_64-3.8/pygame
    copying src_py/_dummybackend.py -> build/lib.macosx-10.9-x86_64-3.8/pygame
    creating build/lib.macosx-10.9-x86_64-3.8/pygame/threads
    copying src_py/threads/Py25Queue.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/threads
    copying src_py/threads/__init__.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/threads
    creating build/lib.macosx-10.9-x86_64-3.8/pygame/tests
    copying test/base_test.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/tests
    copying test/font_test.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/tests
    copying test/mixer_test.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/tests
    copying test/rwobject_test.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/tests
    copying test/pixelcopy_test.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/tests
    copying test/overlay_test.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/tests
    copying test/scrap_test.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/tests
    copying test/touch_tags.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/tests
    copying test/imageext_tags.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/tests
    copying test/pixelarray_test.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/tests
    copying test/draw_test.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/tests
    copying test/transform_test.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/tests
    copying test/blit_test.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/tests
    copying test/bufferproxy_test.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/tests
    copying test/surfarray_test.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/tests
    copying test/mouse_test.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/tests
    copying test/surfarray_tags.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/tests
    copying test/event_test.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/tests
    copying test/imageext_test.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/tests
    copying test/sprite_test.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/tests
    copying test/touch_test.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/tests
    copying test/gfxdraw_test.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/tests
    copying test/rect_test.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/tests
    copying test/scrap_tags.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/tests
    copying test/__init__.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/tests
    copying test/overlay_tags.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/tests
    copying test/color_test.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/tests
    copying test/camera_test.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/tests
    copying test/surflock_test.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/tests
    copying test/key_test.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/tests
    copying test/sysfont_test.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/tests
    copying test/font_tags.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/tests
    copying test/mixer_tags.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/tests
    copying test/constants_test.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/tests
    copying test/mixer_music_tags.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/tests
    copying test/sndarray_test.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/tests
    copying test/image_test.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/tests
    copying test/version_test.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/tests
    copying test/freetype_test.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/tests
    copying test/joystick_test.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/tests
    copying test/midi_tags.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/tests
    copying test/ftfont_tags.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/tests
    copying test/image__save_gl_surface_test.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/tests
    copying test/cdrom_tags.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/tests
    copying test/cursors_test.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/tests
    copying test/fastevent_tags.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/tests
    copying test/display_test.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/tests
    copying test/fastevent_test.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/tests
    copying test/compat_test.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/tests
    copying test/ftfont_test.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/tests
    copying test/cdrom_test.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/tests
    copying test/mask_test.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/tests
    copying test/midi_test.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/tests
    copying test/freetype_tags.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/tests
    copying test/math_test.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/tests
    copying test/time_test.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/tests
    copying test/image_tags.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/tests
    copying test/threads_test.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/tests
    copying test/__main__.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/tests
    copying test/mixer_music_test.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/tests
    copying test/sndarray_tags.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/tests
    copying test/test_test_.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/tests
    copying test/surface_test.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/tests
    creating build/lib.macosx-10.9-x86_64-3.8/pygame/tests/test_utils
    copying test/test_utils/run_tests.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/tests/test_utils
    copying test/test_utils/endian.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/tests/test_utils
    copying test/test_utils/test_machinery.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/tests/test_utils
    copying test/test_utils/__init__.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/tests/test_utils
    copying test/test_utils/png.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/tests/test_utils
    copying test/test_utils/test_runner.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/tests/test_utils
    copying test/test_utils/arrinter.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/tests/test_utils
    copying test/test_utils/buftools.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/tests/test_utils
    copying test/test_utils/async_sub.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/tests/test_utils
    creating build/lib.macosx-10.9-x86_64-3.8/pygame/tests/run_tests__tests
    copying test/run_tests__tests/run_tests__test.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/tests/run_tests__tests
    copying test/run_tests__tests/__init__.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/tests/run_tests__tests
    creating build/lib.macosx-10.9-x86_64-3.8/pygame/tests/run_tests__tests/all_ok
    copying test/run_tests__tests/all_ok/fake_3_test.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/tests/run_tests__tests/all_ok
    copying test/run_tests__tests/all_ok/fake_2_test.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/tests/run_tests__tests/all_ok
    copying test/run_tests__tests/all_ok/__init__.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/tests/run_tests__tests/all_ok
    copying test/run_tests__tests/all_ok/fake_4_test.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/tests/run_tests__tests/all_ok
    copying test/run_tests__tests/all_ok/fake_5_test.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/tests/run_tests__tests/all_ok
    copying test/run_tests__tests/all_ok/no_assertions__ret_code_of_1__test.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/tests/run_tests__tests/all_ok
    copying test/run_tests__tests/all_ok/zero_tests_test.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/tests/run_tests__tests/all_ok
    copying test/run_tests__tests/all_ok/fake_6_test.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/tests/run_tests__tests/all_ok
    creating build/lib.macosx-10.9-x86_64-3.8/pygame/tests/run_tests__tests/failures1
    copying test/run_tests__tests/failures1/fake_3_test.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/tests/run_tests__tests/failures1
    copying test/run_tests__tests/failures1/fake_2_test.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/tests/run_tests__tests/failures1
    copying test/run_tests__tests/failures1/__init__.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/tests/run_tests__tests/failures1
    copying test/run_tests__tests/failures1/fake_4_test.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/tests/run_tests__tests/failures1
    creating build/lib.macosx-10.9-x86_64-3.8/pygame/tests/run_tests__tests/incomplete
    copying test/run_tests__tests/incomplete/fake_3_test.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/tests/run_tests__tests/incomplete
    copying test/run_tests__tests/incomplete/fake_2_test.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/tests/run_tests__tests/incomplete
    copying test/run_tests__tests/incomplete/__init__.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/tests/run_tests__tests/incomplete
    creating build/lib.macosx-10.9-x86_64-3.8/pygame/tests/run_tests__tests/infinite_loop
    copying test/run_tests__tests/infinite_loop/fake_2_test.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/tests/run_tests__tests/infinite_loop
    copying test/run_tests__tests/infinite_loop/fake_1_test.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/tests/run_tests__tests/infinite_loop
    copying test/run_tests__tests/infinite_loop/__init__.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/tests/run_tests__tests/infinite_loop
    creating build/lib.macosx-10.9-x86_64-3.8/pygame/tests/run_tests__tests/print_stderr
    copying test/run_tests__tests/print_stderr/fake_3_test.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/tests/run_tests__tests/print_stderr
    copying test/run_tests__tests/print_stderr/fake_2_test.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/tests/run_tests__tests/print_stderr
    copying test/run_tests__tests/print_stderr/__init__.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/tests/run_tests__tests/print_stderr
    copying test/run_tests__tests/print_stderr/fake_4_test.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/tests/run_tests__tests/print_stderr
    creating build/lib.macosx-10.9-x86_64-3.8/pygame/tests/run_tests__tests/print_stdout
    copying test/run_tests__tests/print_stdout/fake_3_test.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/tests/run_tests__tests/print_stdout
    copying test/run_tests__tests/print_stdout/fake_2_test.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/tests/run_tests__tests/print_stdout
    copying test/run_tests__tests/print_stdout/__init__.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/tests/run_tests__tests/print_stdout
    copying test/run_tests__tests/print_stdout/fake_4_test.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/tests/run_tests__tests/print_stdout
    creating build/lib.macosx-10.9-x86_64-3.8/pygame/tests/run_tests__tests/incomplete_todo
    copying test/run_tests__tests/incomplete_todo/fake_3_test.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/tests/run_tests__tests/incomplete_todo
    copying test/run_tests__tests/incomplete_todo/fake_2_test.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/tests/run_tests__tests/incomplete_todo
    copying test/run_tests__tests/incomplete_todo/__init__.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/tests/run_tests__tests/incomplete_todo
    creating build/lib.macosx-10.9-x86_64-3.8/pygame/tests/run_tests__tests/exclude
    copying test/run_tests__tests/exclude/magic_tag_test.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/tests/run_tests__tests/exclude
    copying test/run_tests__tests/exclude/fake_2_test.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/tests/run_tests__tests/exclude
    copying test/run_tests__tests/exclude/__init__.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/tests/run_tests__tests/exclude
    copying test/run_tests__tests/exclude/invisible_tag_test.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/tests/run_tests__tests/exclude
    creating build/lib.macosx-10.9-x86_64-3.8/pygame/tests/run_tests__tests/timeout
    copying test/run_tests__tests/timeout/sleep_test.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/tests/run_tests__tests/timeout
    copying test/run_tests__tests/timeout/fake_2_test.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/tests/run_tests__tests/timeout
    copying test/run_tests__tests/timeout/__init__.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/tests/run_tests__tests/timeout
    creating build/lib.macosx-10.9-x86_64-3.8/pygame/tests/run_tests__tests/everything
    copying test/run_tests__tests/everything/sleep_test.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/tests/run_tests__tests/everything
    copying test/run_tests__tests/everything/magic_tag_test.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/tests/run_tests__tests/everything
    copying test/run_tests__tests/everything/fake_2_test.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/tests/run_tests__tests/everything
    copying test/run_tests__tests/everything/incomplete_todo_test.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/tests/run_tests__tests/everything
    copying test/run_tests__tests/everything/__init__.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/tests/run_tests__tests/everything
    creating build/lib.macosx-10.9-x86_64-3.8/pygame/docs
    copying docs/__init__.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/docs
    copying docs/__main__.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/docs
    creating build/lib.macosx-10.9-x86_64-3.8/pygame/examples
    copying examples/playmus.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/examples
    copying examples/mask.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/examples
    copying examples/sound.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/examples
    copying examples/overlay.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/examples
    copying examples/aacircle.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/examples
    copying examples/chimp.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/examples
    copying examples/liquid.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/examples
    copying examples/audiocapture.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/examples
    copying examples/sound_array_demos.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/examples
    copying examples/midi.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/examples
    copying examples/scroll.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/examples
    copying examples/cursors.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/examples
    copying examples/moveit.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/examples
    copying examples/__init__.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/examples
    copying examples/blit_blends.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/examples
    copying examples/testsprite.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/examples
    copying examples/textinput.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/examples
    copying examples/vgrade.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/examples
    copying examples/arraydemo.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/examples
    copying examples/stars.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/examples
    copying examples/camera.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/examples
    copying examples/blend_fill.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/examples
    copying examples/fonty.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/examples
    copying examples/headless_no_windows_needed.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/examples
    copying examples/fastevents.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/examples
    copying examples/prevent_display_stretching.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/examples
    copying examples/glcube.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/examples
    copying examples/aliens.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/examples
    copying examples/freetype_misc.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/examples
    copying examples/scaletest.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/examples
    copying examples/video.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/examples
    copying examples/eventlist.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/examples
    copying examples/scrap_clipboard.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/examples
    copying examples/oldalien.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/examples
    copying examples/pixelarray.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/examples
    copying examples/dropevent.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/examples
    running build_ext
    building 'pygame.gfxdraw' extension
    creating build/temp.macosx-10.9-x86_64-3.8
    creating build/temp.macosx-10.9-x86_64-3.8/src_c
    creating build/temp.macosx-10.9-x86_64-3.8/src_c/SDL_gfx
    gcc -Wno-unused-result -Wsign-compare -Wunreachable-code -fno-common -dynamic -DNDEBUG -g -fwrapv -O3 -Wall -arch x86_64 -g -DENABLE_NEWBUF=1 -I/NEED_INC_PATH_FIX -I/Library/Frameworks/Python.framework/Versions/3.8/include/python3.8 -c src_c/gfxdraw.c -o build/temp.macosx-10.9-x86_64-3.8/src_c/gfxdraw.o
    In file included from src_c/gfxdraw.c:33:
    In file included from src_c/pygame.h:32:
    src_c/_pygame.h:216:10: fatal error: 'SDL.h' file not found
    #include <SDL.h>
             ^~~~~~~
    1 error generated.
    ---
    For help with compilation see:
        https://www.pygame.org/wiki/MacCompile
    To contribute to pygame development see:
        https://www.pygame.org/contribute.html
    ---
    error: command 'gcc' failed with exit status 1
    ----------------------------------------
ERROR: Command errored out with exit status 1: /usr/local/bin/python3.8 -u -c 'import sys, setuptools, tokenize; sys.argv[0] = '"'"'/private/var/folders/_7/5n355t_9
MacBook-Pro-de-Spart:tp7 spart$ pip3 install pygame
Collecting pygame
  Using cached pygame-1.9.6.tar.gz (3.2 MB)
Building wheels for collected packages: pygame
  Building wheel for pygame (setup.py) ... error
  ERROR: Command errored out with exit status 1:
   command: /usr/local/bin/python3.8 -u -c 'import sys, setuptools, tokenize; sys.argv[0] = '"'"'/private/var/folders/_7/5n355t_90h1_313mp_ly99kc0000gn/T/pip-install-fr98og2z/pygame/setup.py'"'"'; __file__='"'"'/private/var/folders/_7/5n355t_90h1_313mp_ly99kc0000gn/T/pip-install-fr98og2z/pygame/setup.py'"'"';f=getattr(tokenize, '"'"'open'"'"', open)(__file__);code=f.read().replace('"'"'\r\n'"'"', '"'"'\n'"'"');f.close();exec(compile(code, __file__, '"'"'exec'"'"'))' bdist_wheel -d /private/var/folders/_7/5n355t_90h1_313mp_ly99kc0000gn/T/pip-wheel-w9hvnosb
       cwd: /private/var/folders/_7/5n355t_90h1_313mp_ly99kc0000gn/T/pip-install-fr98og2z/pygame/
  Complete output (218 lines):
  running bdist_wheel
  running build
  running build_py
  creating build
  creating build/lib.macosx-10.9-x86_64-3.8
  creating build/lib.macosx-10.9-x86_64-3.8/pygame
  copying src_py/surfarray.py -> build/lib.macosx-10.9-x86_64-3.8/pygame
  copying src_py/sysfont.py -> build/lib.macosx-10.9-x86_64-3.8/pygame
  copying src_py/_camera_vidcapture.py -> build/lib.macosx-10.9-x86_64-3.8/pygame
  copying src_py/sndarray.py -> build/lib.macosx-10.9-x86_64-3.8/pygame
  copying src_py/version.py -> build/lib.macosx-10.9-x86_64-3.8/pygame
  copying src_py/compat.py -> build/lib.macosx-10.9-x86_64-3.8/pygame
  copying src_py/draw_py.py -> build/lib.macosx-10.9-x86_64-3.8/pygame
  copying src_py/colordict.py -> build/lib.macosx-10.9-x86_64-3.8/pygame
  copying src_py/ftfont.py -> build/lib.macosx-10.9-x86_64-3.8/pygame
  copying src_py/midi.py -> build/lib.macosx-10.9-x86_64-3.8/pygame
  copying src_py/cursors.py -> build/lib.macosx-10.9-x86_64-3.8/pygame
  copying src_py/__init__.py -> build/lib.macosx-10.9-x86_64-3.8/pygame
  copying src_py/_numpysndarray.py -> build/lib.macosx-10.9-x86_64-3.8/pygame
  copying src_py/sprite.py -> build/lib.macosx-10.9-x86_64-3.8/pygame
  copying src_py/macosx.py -> build/lib.macosx-10.9-x86_64-3.8/pygame
  copying src_py/_numpysurfarray.py -> build/lib.macosx-10.9-x86_64-3.8/pygame
  copying src_py/camera.py -> build/lib.macosx-10.9-x86_64-3.8/pygame
  copying src_py/freetype.py -> build/lib.macosx-10.9-x86_64-3.8/pygame
  copying src_py/_camera_opencv_highgui.py -> build/lib.macosx-10.9-x86_64-3.8/pygame
  copying src_py/pkgdata.py -> build/lib.macosx-10.9-x86_64-3.8/pygame
  copying src_py/locals.py -> build/lib.macosx-10.9-x86_64-3.8/pygame
  copying src_py/_dummybackend.py -> build/lib.macosx-10.9-x86_64-3.8/pygame
  creating build/lib.macosx-10.9-x86_64-3.8/pygame/threads
  copying src_py/threads/Py25Queue.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/threads
  copying src_py/threads/__init__.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/threads
  creating build/lib.macosx-10.9-x86_64-3.8/pygame/tests
  copying test/base_test.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/tests
  copying test/font_test.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/tests
  copying test/mixer_test.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/tests
  copying test/rwobject_test.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/tests
  copying test/pixelcopy_test.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/tests
  copying test/overlay_test.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/tests
  copying test/scrap_test.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/tests
  copying test/touch_tags.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/tests
  copying test/imageext_tags.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/tests
  copying test/pixelarray_test.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/tests
  copying test/draw_test.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/tests
  copying test/transform_test.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/tests
  copying test/blit_test.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/tests
  copying test/bufferproxy_test.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/tests
  copying test/surfarray_test.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/tests
  copying test/mouse_test.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/tests
  copying test/surfarray_tags.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/tests
  copying test/event_test.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/tests
  copying test/imageext_test.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/tests
  copying test/sprite_test.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/tests
  copying test/touch_test.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/tests
  copying test/gfxdraw_test.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/tests
  copying test/rect_test.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/tests
  copying test/scrap_tags.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/tests
  copying test/__init__.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/tests
  copying test/overlay_tags.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/tests
  copying test/color_test.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/tests
  copying test/camera_test.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/tests
  copying test/surflock_test.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/tests
  copying test/key_test.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/tests
  copying test/sysfont_test.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/tests
  copying test/font_tags.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/tests
  copying test/mixer_tags.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/tests
  copying test/constants_test.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/tests
  copying test/mixer_music_tags.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/tests
  copying test/sndarray_test.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/tests
  copying test/image_test.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/tests
  copying test/version_test.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/tests
  copying test/freetype_test.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/tests
  copying test/joystick_test.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/tests
  copying test/midi_tags.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/tests
  copying test/ftfont_tags.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/tests
  copying test/image__save_gl_surface_test.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/tests
  copying test/cdrom_tags.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/tests
  copying test/cursors_test.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/tests
  copying test/fastevent_tags.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/tests
  copying test/display_test.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/tests
  copying test/fastevent_test.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/tests
  copying test/compat_test.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/tests
  copying test/ftfont_test.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/tests
  copying test/cdrom_test.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/tests
  copying test/mask_test.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/tests
  copying test/midi_test.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/tests
  copying test/freetype_tags.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/tests
  copying test/math_test.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/tests
  copying test/time_test.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/tests
  copying test/image_tags.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/tests
  copying test/threads_test.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/tests
  copying test/__main__.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/tests
  copying test/mixer_music_test.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/tests
  copying test/sndarray_tags.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/tests
  copying test/test_test_.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/tests
  copying test/surface_test.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/tests
  creating build/lib.macosx-10.9-x86_64-3.8/pygame/tests/test_utils
  copying test/test_utils/run_tests.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/tests/test_utils
  copying test/test_utils/endian.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/tests/test_utils
  copying test/test_utils/test_machinery.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/tests/test_utils
  copying test/test_utils/__init__.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/tests/test_utils
  copying test/test_utils/png.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/tests/test_utils
  copying test/test_utils/test_runner.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/tests/test_utils
  copying test/test_utils/arrinter.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/tests/test_utils
  copying test/test_utils/buftools.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/tests/test_utils
  copying test/test_utils/async_sub.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/tests/test_utils
  creating build/lib.macosx-10.9-x86_64-3.8/pygame/tests/run_tests__tests
  copying test/run_tests__tests/run_tests__test.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/tests/run_tests__tests
  copying test/run_tests__tests/__init__.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/tests/run_tests__tests
  creating build/lib.macosx-10.9-x86_64-3.8/pygame/tests/run_tests__tests/all_ok
  copying test/run_tests__tests/all_ok/fake_3_test.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/tests/run_tests__tests/all_ok
  copying test/run_tests__tests/all_ok/fake_2_test.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/tests/run_tests__tests/all_ok
  copying test/run_tests__tests/all_ok/__init__.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/tests/run_tests__tests/all_ok
  copying test/run_tests__tests/all_ok/fake_4_test.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/tests/run_tests__tests/all_ok
  copying test/run_tests__tests/all_ok/fake_5_test.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/tests/run_tests__tests/all_ok
  copying test/run_tests__tests/all_ok/no_assertions__ret_code_of_1__test.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/tests/run_tests__tests/all_ok
  copying test/run_tests__tests/all_ok/zero_tests_test.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/tests/run_tests__tests/all_ok
  copying test/run_tests__tests/all_ok/fake_6_test.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/tests/run_tests__tests/all_ok
  creating build/lib.macosx-10.9-x86_64-3.8/pygame/tests/run_tests__tests/failures1
  copying test/run_tests__tests/failures1/fake_3_test.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/tests/run_tests__tests/failures1
  copying test/run_tests__tests/failures1/fake_2_test.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/tests/run_tests__tests/failures1
  copying test/run_tests__tests/failures1/__init__.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/tests/run_tests__tests/failures1
  copying test/run_tests__tests/failures1/fake_4_test.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/tests/run_tests__tests/failures1
  creating build/lib.macosx-10.9-x86_64-3.8/pygame/tests/run_tests__tests/incomplete
  copying test/run_tests__tests/incomplete/fake_3_test.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/tests/run_tests__tests/incomplete
  copying test/run_tests__tests/incomplete/fake_2_test.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/tests/run_tests__tests/incomplete
  copying test/run_tests__tests/incomplete/__init__.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/tests/run_tests__tests/incomplete
  creating build/lib.macosx-10.9-x86_64-3.8/pygame/tests/run_tests__tests/infinite_loop
  copying test/run_tests__tests/infinite_loop/fake_2_test.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/tests/run_tests__tests/infinite_loop
  copying test/run_tests__tests/infinite_loop/fake_1_test.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/tests/run_tests__tests/infinite_loop
  copying test/run_tests__tests/infinite_loop/__init__.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/tests/run_tests__tests/infinite_loop
  creating build/lib.macosx-10.9-x86_64-3.8/pygame/tests/run_tests__tests/print_stderr
  copying test/run_tests__tests/print_stderr/fake_3_test.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/tests/run_tests__tests/print_stderr
  copying test/run_tests__tests/print_stderr/fake_2_test.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/tests/run_tests__tests/print_stderr
  copying test/run_tests__tests/print_stderr/__init__.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/tests/run_tests__tests/print_stderr
  copying test/run_tests__tests/print_stderr/fake_4_test.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/tests/run_tests__tests/print_stderr
  creating build/lib.macosx-10.9-x86_64-3.8/pygame/tests/run_tests__tests/print_stdout
  copying test/run_tests__tests/print_stdout/fake_3_test.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/tests/run_tests__tests/print_stdout
  copying test/run_tests__tests/print_stdout/fake_2_test.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/tests/run_tests__tests/print_stdout
  copying test/run_tests__tests/print_stdout/__init__.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/tests/run_tests__tests/print_stdout
  copying test/run_tests__tests/print_stdout/fake_4_test.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/tests/run_tests__tests/print_stdout
  creating build/lib.macosx-10.9-x86_64-3.8/pygame/tests/run_tests__tests/incomplete_todo
  copying test/run_tests__tests/incomplete_todo/fake_3_test.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/tests/run_tests__tests/incomplete_todo
  copying test/run_tests__tests/incomplete_todo/fake_2_test.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/tests/run_tests__tests/incomplete_todo
  copying test/run_tests__tests/incomplete_todo/__init__.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/tests/run_tests__tests/incomplete_todo
  creating build/lib.macosx-10.9-x86_64-3.8/pygame/tests/run_tests__tests/exclude
  copying test/run_tests__tests/exclude/magic_tag_test.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/tests/run_tests__tests/exclude
  copying test/run_tests__tests/exclude/fake_2_test.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/tests/run_tests__tests/exclude
  copying test/run_tests__tests/exclude/__init__.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/tests/run_tests__tests/exclude
  copying test/run_tests__tests/exclude/invisible_tag_test.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/tests/run_tests__tests/exclude
  creating build/lib.macosx-10.9-x86_64-3.8/pygame/tests/run_tests__tests/timeout
  copying test/run_tests__tests/timeout/sleep_test.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/tests/run_tests__tests/timeout
  copying test/run_tests__tests/timeout/fake_2_test.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/tests/run_tests__tests/timeout
  copying test/run_tests__tests/timeout/__init__.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/tests/run_tests__tests/timeout
  creating build/lib.macosx-10.9-x86_64-3.8/pygame/tests/run_tests__tests/everything
  copying test/run_tests__tests/everything/sleep_test.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/tests/run_tests__tests/everything
  copying test/run_tests__tests/everything/magic_tag_test.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/tests/run_tests__tests/everything
  copying test/run_tests__tests/everything/fake_2_test.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/tests/run_tests__tests/everything
  copying test/run_tests__tests/everything/incomplete_todo_test.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/tests/run_tests__tests/everything
  copying test/run_tests__tests/everything/__init__.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/tests/run_tests__tests/everything
  creating build/lib.macosx-10.9-x86_64-3.8/pygame/docs
  copying docs/__init__.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/docs
  copying docs/__main__.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/docs
  creating build/lib.macosx-10.9-x86_64-3.8/pygame/examples
  copying examples/playmus.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/examples
  copying examples/mask.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/examples
  copying examples/sound.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/examples
  copying examples/overlay.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/examples
  copying examples/aacircle.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/examples
  copying examples/chimp.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/examples
  copying examples/liquid.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/examples
  copying examples/audiocapture.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/examples
  copying examples/sound_array_demos.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/examples
  copying examples/midi.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/examples
  copying examples/scroll.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/examples
  copying examples/cursors.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/examples
  copying examples/moveit.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/examples
  copying examples/__init__.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/examples
  copying examples/blit_blends.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/examples
  copying examples/testsprite.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/examples
  copying examples/textinput.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/examples
  copying examples/vgrade.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/examples
  copying examples/arraydemo.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/examples
  copying examples/stars.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/examples
  copying examples/camera.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/examples
  copying examples/blend_fill.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/examples
  copying examples/fonty.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/examples
  copying examples/headless_no_windows_needed.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/examples
  copying examples/fastevents.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/examples
  copying examples/prevent_display_stretching.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/examples
  copying examples/glcube.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/examples
  copying examples/aliens.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/examples
  copying examples/freetype_misc.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/examples
  copying examples/scaletest.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/examples
  copying examples/video.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/examples
  copying examples/eventlist.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/examples
  copying examples/scrap_clipboard.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/examples
  copying examples/oldalien.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/examples
  copying examples/pixelarray.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/examples
  copying examples/dropevent.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/examples
  running build_ext
  building 'pygame.gfxdraw' extension
  creating build/temp.macosx-10.9-x86_64-3.8
  creating build/temp.macosx-10.9-x86_64-3.8/src_c
  creating build/temp.macosx-10.9-x86_64-3.8/src_c/SDL_gfx
  gcc -Wno-unused-result -Wsign-compare -Wunreachable-code -fno-common -dynamic -DNDEBUG -g -fwrapv -O3 -Wall -arch x86_64 -g -DENABLE_NEWBUF=1 -I/NEED_INC_PATH_FIX -I/Library/Frameworks/Python.framework/Versions/3.8/include/python3.8 -c src_c/gfxdraw.c -o build/temp.macosx-10.9-x86_64-3.8/src_c/gfxdraw.o
  In file included from src_c/gfxdraw.c:33:
  In file included from src_c/pygame.h:32:
  src_c/_pygame.h:216:10: fatal error: 'SDL.h' file not found
  #include <SDL.h>
           ^~~~~~~
  1 error generated.
  ---
  For help with compilation see:
      https://www.pygame.org/wiki/MacCompile
  To contribute to pygame development see:
      https://www.pygame.org/contribute.html
  ---
  error: command 'gcc' failed with exit status 1
  ----------------------------------------
  ERROR: Failed building wheel for pygame
  Running setup.py clean for pygame
Failed to build pygame
Installing collected packages: pygame
    Running setup.py install for pygame ... error
    ERROR: Command errored out with exit status 1:
     command: /usr/local/bin/python3.8 -u -c 'import sys, setuptools, tokenize; sys.argv[0] = '"'"'/private/var/folders/_7/5n355t_90h1_313mp_ly99kc0000gn/T/pip-install-fr98og2z/pygame/setup.py'"'"'; __file__='"'"'/private/var/folders/_7/5n355t_90h1_313mp_ly99kc0000gn/T/pip-install-fr98og2z/pygame/setup.py'"'"';f=getattr(tokenize, '"'"'open'"'"', open)(__file__);code=f.read().replace('"'"'\r\n'"'"', '"'"'\n'"'"');f.close();exec(compile(code, __file__, '"'"'exec'"'"'))' install --record /private/var/folders/_7/5n355t_90h1_313mp_ly99kc0000gn/T/pip-record-8gbi7mkm/install-record.txt --single-version-externally-managed --compile --install-headers /Library/Frameworks/Python.framework/Versions/3.8/include/python3.8/pygame
         cwd: /private/var/folders/_7/5n355t_90h1_313mp_ly99kc0000gn/T/pip-install-fr98og2z/pygame/
    Complete output (218 lines):
    running install
    running build
    running build_py
    creating build
    creating build/lib.macosx-10.9-x86_64-3.8
    creating build/lib.macosx-10.9-x86_64-3.8/pygame
    copying src_py/surfarray.py -> build/lib.macosx-10.9-x86_64-3.8/pygame
    copying src_py/sysfont.py -> build/lib.macosx-10.9-x86_64-3.8/pygame
    copying src_py/_camera_vidcapture.py -> build/lib.macosx-10.9-x86_64-3.8/pygame
    copying src_py/sndarray.py -> build/lib.macosx-10.9-x86_64-3.8/pygame
    copying src_py/version.py -> build/lib.macosx-10.9-x86_64-3.8/pygame
    copying src_py/compat.py -> build/lib.macosx-10.9-x86_64-3.8/pygame
    copying src_py/draw_py.py -> build/lib.macosx-10.9-x86_64-3.8/pygame
    copying src_py/colordict.py -> build/lib.macosx-10.9-x86_64-3.8/pygame
    copying src_py/ftfont.py -> build/lib.macosx-10.9-x86_64-3.8/pygame
    copying src_py/midi.py -> build/lib.macosx-10.9-x86_64-3.8/pygame
    copying src_py/cursors.py -> build/lib.macosx-10.9-x86_64-3.8/pygame
    copying src_py/__init__.py -> build/lib.macosx-10.9-x86_64-3.8/pygame
    copying src_py/_numpysndarray.py -> build/lib.macosx-10.9-x86_64-3.8/pygame
    copying src_py/sprite.py -> build/lib.macosx-10.9-x86_64-3.8/pygame
    copying src_py/macosx.py -> build/lib.macosx-10.9-x86_64-3.8/pygame
    copying src_py/_numpysurfarray.py -> build/lib.macosx-10.9-x86_64-3.8/pygame
    copying src_py/camera.py -> build/lib.macosx-10.9-x86_64-3.8/pygame
    copying src_py/freetype.py -> build/lib.macosx-10.9-x86_64-3.8/pygame
    copying src_py/_camera_opencv_highgui.py -> build/lib.macosx-10.9-x86_64-3.8/pygame
    copying src_py/pkgdata.py -> build/lib.macosx-10.9-x86_64-3.8/pygame
    copying src_py/locals.py -> build/lib.macosx-10.9-x86_64-3.8/pygame
    copying src_py/_dummybackend.py -> build/lib.macosx-10.9-x86_64-3.8/pygame
    creating build/lib.macosx-10.9-x86_64-3.8/pygame/threads
    copying src_py/threads/Py25Queue.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/threads
    copying src_py/threads/__init__.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/threads
    creating build/lib.macosx-10.9-x86_64-3.8/pygame/tests
    copying test/base_test.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/tests
    copying test/font_test.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/tests
    copying test/mixer_test.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/tests
    copying test/rwobject_test.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/tests
    copying test/pixelcopy_test.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/tests
    copying test/overlay_test.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/tests
    copying test/scrap_test.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/tests
    copying test/touch_tags.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/tests
    copying test/imageext_tags.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/tests
    copying test/pixelarray_test.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/tests
    copying test/draw_test.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/tests
    copying test/transform_test.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/tests
    copying test/blit_test.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/tests
    copying test/bufferproxy_test.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/tests
    copying test/surfarray_test.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/tests
    copying test/mouse_test.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/tests
    copying test/surfarray_tags.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/tests
    copying test/event_test.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/tests
    copying test/imageext_test.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/tests
    copying test/sprite_test.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/tests
    copying test/touch_test.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/tests
    copying test/gfxdraw_test.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/tests
    copying test/rect_test.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/tests
    copying test/scrap_tags.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/tests
    copying test/__init__.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/tests
    copying test/overlay_tags.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/tests
    copying test/color_test.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/tests
    copying test/camera_test.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/tests
    copying test/surflock_test.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/tests
    copying test/key_test.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/tests
    copying test/sysfont_test.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/tests
    copying test/font_tags.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/tests
    copying test/mixer_tags.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/tests
    copying test/constants_test.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/tests
    copying test/mixer_music_tags.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/tests
    copying test/sndarray_test.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/tests
    copying test/image_test.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/tests
    copying test/version_test.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/tests
    copying test/freetype_test.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/tests
    copying test/joystick_test.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/tests
    copying test/midi_tags.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/tests
    copying test/ftfont_tags.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/tests
    copying test/image__save_gl_surface_test.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/tests
    copying test/cdrom_tags.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/tests
    copying test/cursors_test.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/tests
    copying test/fastevent_tags.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/tests
    copying test/display_test.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/tests
    copying test/fastevent_test.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/tests
    copying test/compat_test.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/tests
    copying test/ftfont_test.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/tests
    copying test/cdrom_test.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/tests
    copying test/mask_test.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/tests
    copying test/midi_test.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/tests
    copying test/freetype_tags.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/tests
    copying test/math_test.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/tests
    copying test/time_test.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/tests
    copying test/image_tags.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/tests
    copying test/threads_test.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/tests
    copying test/__main__.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/tests
    copying test/mixer_music_test.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/tests
    copying test/sndarray_tags.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/tests
    copying test/test_test_.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/tests
    copying test/surface_test.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/tests
    creating build/lib.macosx-10.9-x86_64-3.8/pygame/tests/test_utils
    copying test/test_utils/run_tests.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/tests/test_utils
    copying test/test_utils/endian.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/tests/test_utils
    copying test/test_utils/test_machinery.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/tests/test_utils
    copying test/test_utils/__init__.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/tests/test_utils
    copying test/test_utils/png.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/tests/test_utils
    copying test/test_utils/test_runner.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/tests/test_utils
    copying test/test_utils/arrinter.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/tests/test_utils
    copying test/test_utils/buftools.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/tests/test_utils
    copying test/test_utils/async_sub.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/tests/test_utils
    creating build/lib.macosx-10.9-x86_64-3.8/pygame/tests/run_tests__tests
    copying test/run_tests__tests/run_tests__test.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/tests/run_tests__tests
    copying test/run_tests__tests/__init__.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/tests/run_tests__tests
    creating build/lib.macosx-10.9-x86_64-3.8/pygame/tests/run_tests__tests/all_ok
    copying test/run_tests__tests/all_ok/fake_3_test.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/tests/run_tests__tests/all_ok
    copying test/run_tests__tests/all_ok/fake_2_test.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/tests/run_tests__tests/all_ok
    copying test/run_tests__tests/all_ok/__init__.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/tests/run_tests__tests/all_ok
    copying test/run_tests__tests/all_ok/fake_4_test.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/tests/run_tests__tests/all_ok
    copying test/run_tests__tests/all_ok/fake_5_test.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/tests/run_tests__tests/all_ok
    copying test/run_tests__tests/all_ok/no_assertions__ret_code_of_1__test.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/tests/run_tests__tests/all_ok
    copying test/run_tests__tests/all_ok/zero_tests_test.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/tests/run_tests__tests/all_ok
    copying test/run_tests__tests/all_ok/fake_6_test.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/tests/run_tests__tests/all_ok
    creating build/lib.macosx-10.9-x86_64-3.8/pygame/tests/run_tests__tests/failures1
    copying test/run_tests__tests/failures1/fake_3_test.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/tests/run_tests__tests/failures1
    copying test/run_tests__tests/failures1/fake_2_test.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/tests/run_tests__tests/failures1
    copying test/run_tests__tests/failures1/__init__.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/tests/run_tests__tests/failures1
    copying test/run_tests__tests/failures1/fake_4_test.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/tests/run_tests__tests/failures1
    creating build/lib.macosx-10.9-x86_64-3.8/pygame/tests/run_tests__tests/incomplete
    copying test/run_tests__tests/incomplete/fake_3_test.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/tests/run_tests__tests/incomplete
    copying test/run_tests__tests/incomplete/fake_2_test.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/tests/run_tests__tests/incomplete
    copying test/run_tests__tests/incomplete/__init__.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/tests/run_tests__tests/incomplete
    creating build/lib.macosx-10.9-x86_64-3.8/pygame/tests/run_tests__tests/infinite_loop
    copying test/run_tests__tests/infinite_loop/fake_2_test.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/tests/run_tests__tests/infinite_loop
    copying test/run_tests__tests/infinite_loop/fake_1_test.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/tests/run_tests__tests/infinite_loop
    copying test/run_tests__tests/infinite_loop/__init__.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/tests/run_tests__tests/infinite_loop
    creating build/lib.macosx-10.9-x86_64-3.8/pygame/tests/run_tests__tests/print_stderr
    copying test/run_tests__tests/print_stderr/fake_3_test.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/tests/run_tests__tests/print_stderr
    copying test/run_tests__tests/print_stderr/fake_2_test.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/tests/run_tests__tests/print_stderr
    copying test/run_tests__tests/print_stderr/__init__.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/tests/run_tests__tests/print_stderr
    copying test/run_tests__tests/print_stderr/fake_4_test.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/tests/run_tests__tests/print_stderr
    creating build/lib.macosx-10.9-x86_64-3.8/pygame/tests/run_tests__tests/print_stdout
    copying test/run_tests__tests/print_stdout/fake_3_test.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/tests/run_tests__tests/print_stdout
    copying test/run_tests__tests/print_stdout/fake_2_test.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/tests/run_tests__tests/print_stdout
    copying test/run_tests__tests/print_stdout/__init__.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/tests/run_tests__tests/print_stdout
    copying test/run_tests__tests/print_stdout/fake_4_test.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/tests/run_tests__tests/print_stdout
    creating build/lib.macosx-10.9-x86_64-3.8/pygame/tests/run_tests__tests/incomplete_todo
    copying test/run_tests__tests/incomplete_todo/fake_3_test.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/tests/run_tests__tests/incomplete_todo
    copying test/run_tests__tests/incomplete_todo/fake_2_test.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/tests/run_tests__tests/incomplete_todo
    copying test/run_tests__tests/incomplete_todo/__init__.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/tests/run_tests__tests/incomplete_todo
    creating build/lib.macosx-10.9-x86_64-3.8/pygame/tests/run_tests__tests/exclude
    copying test/run_tests__tests/exclude/magic_tag_test.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/tests/run_tests__tests/exclude
    copying test/run_tests__tests/exclude/fake_2_test.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/tests/run_tests__tests/exclude
    copying test/run_tests__tests/exclude/__init__.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/tests/run_tests__tests/exclude
    copying test/run_tests__tests/exclude/invisible_tag_test.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/tests/run_tests__tests/exclude
    creating build/lib.macosx-10.9-x86_64-3.8/pygame/tests/run_tests__tests/timeout
    copying test/run_tests__tests/timeout/sleep_test.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/tests/run_tests__tests/timeout
    copying test/run_tests__tests/timeout/fake_2_test.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/tests/run_tests__tests/timeout
    copying test/run_tests__tests/timeout/__init__.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/tests/run_tests__tests/timeout
    creating build/lib.macosx-10.9-x86_64-3.8/pygame/tests/run_tests__tests/everything
    copying test/run_tests__tests/everything/sleep_test.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/tests/run_tests__tests/everything
    copying test/run_tests__tests/everything/magic_tag_test.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/tests/run_tests__tests/everything
    copying test/run_tests__tests/everything/fake_2_test.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/tests/run_tests__tests/everything
    copying test/run_tests__tests/everything/incomplete_todo_test.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/tests/run_tests__tests/everything
    copying test/run_tests__tests/everything/__init__.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/tests/run_tests__tests/everything
    creating build/lib.macosx-10.9-x86_64-3.8/pygame/docs
    copying docs/__init__.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/docs
    copying docs/__main__.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/docs
    creating build/lib.macosx-10.9-x86_64-3.8/pygame/examples
    copying examples/playmus.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/examples
    copying examples/mask.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/examples
    copying examples/sound.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/examples
    copying examples/overlay.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/examples
    copying examples/aacircle.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/examples
    copying examples/chimp.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/examples
    copying examples/liquid.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/examples
    copying examples/audiocapture.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/examples
    copying examples/sound_array_demos.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/examples
    copying examples/midi.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/examples
    copying examples/scroll.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/examples
    copying examples/cursors.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/examples
    copying examples/moveit.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/examples
    copying examples/__init__.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/examples
    copying examples/blit_blends.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/examples
    copying examples/testsprite.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/examples
    copying examples/textinput.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/examples
    copying examples/vgrade.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/examples
    copying examples/arraydemo.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/examples
    copying examples/stars.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/examples
    copying examples/camera.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/examples
    copying examples/blend_fill.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/examples
    copying examples/fonty.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/examples
    copying examples/headless_no_windows_needed.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/examples
    copying examples/fastevents.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/examples
    copying examples/prevent_display_stretching.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/examples
    copying examples/glcube.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/examples
    copying examples/aliens.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/examples
    copying examples/freetype_misc.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/examples
    copying examples/scaletest.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/examples
    copying examples/video.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/examples
    copying examples/eventlist.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/examples
    copying examples/scrap_clipboard.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/examples
    copying examples/oldalien.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/examples
    copying examples/pixelarray.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/examples
    copying examples/dropevent.py -> build/lib.macosx-10.9-x86_64-3.8/pygame/examples
    running build_ext
    building 'pygame.gfxdraw' extension
    creating build/temp.macosx-10.9-x86_64-3.8
    creating build/temp.macosx-10.9-x86_64-3.8/src_c
    creating build/temp.macosx-10.9-x86_64-3.8/src_c/SDL_gfx
    gcc -Wno-unused-result -Wsign-compare -Wunreachable-code -fno-common -dynamic -DNDEBUG -g -fwrapv -O3 -Wall -arch x86_64 -g -DENABLE_NEWBUF=1 -I/NEED_INC_PATH_FIX -I/Library/Frameworks/Python.framework/Versions/3.8/include/python3.8 -c src_c/gfxdraw.c -o build/temp.macosx-10.9-x86_64-3.8/src_c/gfxdraw.o
    In file included from src_c/gfxdraw.c:33:
    In file included from src_c/pygame.h:32:
    src_c/_pygame.h:216:10: fatal error: 'SDL.h' file not found
    #include <SDL.h>
             ^~~~~~~
    1 error generated.
    ---
    For help with compilation see:
        https://www.pygame.org/wiki/MacCompile
    To contribute to pygame development see:
        https://www.pygame.org/contribute.html
    ---
    error: command 'gcc' failed with exit status 1
    ----------------------------------------
ERROR: Command errored out with exit status 1: /usr/local/bin/python3.8 -u -c 'import sys, setuptools, tokenize; sys.argv[0] = '"'"'/private/var/folders/_7/5n355t_90h1_313mp_ly99kc0000gn/T/pip-install-fr98og2z/pygame/setup.py'"'"'; __file__='"'"'/private/var/folders/_7/5n355t_90h1_313mp_ly99kc0000gn/T/pip-install-fr98og2z/pygame/setup.py'"'"';f=getattr(tokenize, '"'"'open'"'"', open)(__file__);code=f.read().replace('"'"'\r\n'"'"', '"'"'\n'"'"');f.close();exec(compile(code, __file__, '"'"'exec'"'"'))' install --record /private/var/folders/_7/5n355t_90h1_313mp_ly99kc0000gn/T/pip-record-8gbi7mkm/install-record.txt --single-version-externally-managed --compile --install-headers /Library/Frameworks/Python.framework/Versions/3.8/include/python3.8/pygame Check the logs for full command output.
MacBook-Pro-de-Spart:tp7 spart$
