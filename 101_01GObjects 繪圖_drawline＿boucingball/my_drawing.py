"""
File: my_drawing.py
Name:Meg
----------------------
Title:My Neighbor TOTORO

The animation:TOTORO maybe everyone's childhood.
A pure and cute creature.
When I feel lonely, image TOTORO stay with me.
It always make me happy.
"""

from campy.graphics.gobjects import GOval, GRect, GLabel, GArc, GPolygon, GLine
from campy.graphics.gwindow import GWindow


def main():
    """
    TODO:
    """
    window = GWindow(width=800, height=500, title="TOTORO")
    background_night = GRect(800, 500)
    background_night.filled = True
    background_night.fill_color = "midnightblue"
    window.add(background_night)

    moon = GOval(490, 490, x=150, y=5)
    moon.filled = True
    moon.fill_color = "lightyellow"
    moon.color= "lightyellow"
    window.add(moon)

    label_0 = GLabel("My Neighbor \n TOTORO", x=78, y=178)
    label_0.color = "dimgrey"
    label_0.font = "-60"
    window.add(label_0)

    label = GLabel("My Neighbor \n TOTORO", x=80, y=180)
    label.color = "pink"
    label.font = "-60"
    window.add(label)

    cloud = GOval(200, 100, x=50, y=250)
    cloud.filled = True
    cloud.fill_color = "lightgrey"
    cloud.color= "lightgrey"
    window.add(cloud)

    cloud_1 = GOval(100, 100, x=80, y=240)
    cloud_1.filled = True
    cloud_1.fill_color = "lightgrey"
    cloud_1.color = "lightgrey"
    window.add(cloud_1)

    cloud_2 = GOval(90, 90, x=150, y=230)
    cloud_2.filled = True
    cloud_2.fill_color = "lightgrey"
    cloud_2.color = "lightgrey"
    window.add(cloud_2)

    cloud_3 = GOval(80, 80, x=190, y=250)
    cloud_3.filled = True
    cloud_3.fill_color = "lightgrey"
    cloud_3.color = "lightgrey"
    window.add(cloud_3)

    cloud_4 = GOval(80, 80, x=80, y=290)
    cloud_4.filled = True
    cloud_4.fill_color = "lightgrey"
    cloud_4.color = "lightgrey"
    window.add(cloud_4)

    cloud_5 = GOval(60, 60, x=50, y=290)
    cloud_5.filled = True
    cloud_5.fill_color = "lightgrey"
    cloud_5.color = "lightgrey"
    window.add(cloud_5)

    face = GOval(200, 150, x=400, y=100)
    face.filled = True
    face.fill_color = "slategrey"
    face.color = "slategrey"
    window.add(face)

    l_ear = GOval(30, 100, x=420, y=40)
    l_ear.filled = True
    l_ear.fill_color = "slategrey"
    l_ear.color = "slategrey"
    window.add(l_ear)

    l_ear_r = GPolygon()
    l_ear_r.add_vertex((444, 102))
    l_ear_r.add_vertex((454, 97))
    l_ear_r.add_vertex((454, 107))
    l_ear_r.filled = True
    l_ear_r.fill_color = "lightyellow"
    l_ear_r.color = "lightyellow"
    window.add(l_ear_r)

    l_ear_l = GPolygon()
    l_ear_l.add_vertex((418, 110))
    l_ear_l.add_vertex((428, 115))
    l_ear_l.add_vertex((418, 120))
    l_ear_l.filled = True
    l_ear_l.fill_color = "lightyellow"
    l_ear_l.color = "lightyellow"
    window.add(l_ear_l)

    r_ear = GOval(30, 100, x=545, y=40)
    r_ear.filled = True
    r_ear.fill_color = "slategrey"
    r_ear.color = "slategrey"
    window.add(r_ear)

    r_ear_l = GPolygon()
    r_ear_l.add_vertex((541, 95))
    r_ear_l.add_vertex((551, 100))
    r_ear_l.add_vertex((541, 105))
    r_ear_l.filled = True
    r_ear_l.fill_color = "lightyellow"
    r_ear_l.color = "lightyellow"
    window.add(r_ear_l)

    r_ear_r = GPolygon()
    r_ear_r.add_vertex((568, 110))
    r_ear_r.add_vertex((578, 105))
    r_ear_r.add_vertex((578, 115))
    r_ear_r.filled = True
    r_ear_r.fill_color = "lightyellow"
    r_ear_r.color = "lightyellow"
    window.add(r_ear_r)

    body = GOval(290, 270, x=355, y=150)
    body.filled = True
    body.fill_color = "slategrey"
    body.color = "slategrey"
    window.add(body)

    tail = GOval(70, 90, x=465, y=390)
    tail.filled = True
    tail.fill_color = "slategrey"
    tail.color = "slategrey"
    window.add(tail)

    l_hand = GOval(80, 170, x=345, y=200)
    l_hand.filled = True
    l_hand.fill_color = "slategrey"
    l_hand.color = "slategrey"
    window.add(l_hand)

    l_finger_1 = GArc(20, 80, 180, 80, x=370, y=345)
    l_finger_1.filled = True
    l_finger_1.fill_color = "slategrey"
    l_finger_1.color = "slategrey"
    window.add(l_finger_1)

    l_finger_2 = GArc(20, 80, 180, 80, x=380, y=345)
    l_finger_2.filled = True
    l_finger_2.fill_color = "slategrey"
    l_finger_2.color = "slategrey"
    window.add(l_finger_2)

    r_hand = GOval(80, 170, x=580, y=200)
    r_hand.filled = True
    r_hand.fill_color = "slategrey"
    r_hand.color = "slategrey"
    window.add(r_hand)

    r_finger_1 = GArc(20, 80, 270, 80, x=610, y=345)
    r_finger_1.filled = True
    r_finger_1.fill_color = "slategrey"
    r_finger_1.color = "slategrey"
    window.add(r_finger_1)

    r_finger_2 = GArc(20, 80, 270, 80, x=620, y=345)
    r_finger_2.filled = True
    r_finger_2.fill_color = "slategrey"
    r_finger_2.color = "slategrey"
    window.add(r_finger_2)

    tree = GPolygon()
    tree.add_vertex((300, 340))
    tree.add_vertex((400, 400))
    tree.add_vertex((500, 400))
    tree.add_vertex((670, 380))
    tree.add_vertex((800, 470))
    tree.add_vertex((800, 500))
    tree.add_vertex((650, 430))
    tree.add_vertex((500, 450))
    tree.add_vertex((400, 450))
    tree.add_vertex((300, 400))
    tree.filled = True
    tree.fill_color = "sienna"
    tree.color = "sienna"
    window.add(tree)

    belly = GOval(248, 233, x=377, y=185)
    belly.filled = True
    belly.fill_color = "oldlace"
    belly.color = "oldlace"
    window.add(belly)

    pattern_0 = GPolygon()
    pattern_0.add_vertex((412, 235))  # pattern left
    pattern_0.add_vertex((442, 220))  # pattern up
    pattern_0.add_vertex((462, 228))  # pattern right
    pattern_0.add_vertex((442, 225))  # pattern down
    pattern_0.filled = True
    pattern_0.fill_color = "slategrey"
    pattern_0.color ="slategrey"
    window.add(pattern_0)

    pattern_1 = GPolygon()
    pattern_1.add_vertex((470, 225))  # pattern left
    pattern_1.add_vertex((502, 210))  # pattern up
    pattern_1.add_vertex((534, 225))  # pattern right
    pattern_1.add_vertex((502, 215))  # pattern down
    pattern_1.filled = True
    pattern_1.fill_color = "slategrey"
    pattern_1.color = "slategrey"
    window.add(pattern_1)

    pattern_2 = GPolygon()
    pattern_2.add_vertex((542, 228))  # pattern left
    pattern_2.add_vertex((562, 220))  # pattern up
    pattern_2.add_vertex((592, 235))  # pattern right
    pattern_2.add_vertex((562, 225))  # pattern down
    pattern_2.filled = True
    pattern_2.fill_color = "slategrey"
    pattern_2.color = "slategrey"
    window.add(pattern_2)

    pattern_3 = GPolygon()
    pattern_3.add_vertex((400, 265))  # pattern left
    pattern_3.add_vertex((430, 250))  # pattern up
    pattern_3.add_vertex((450, 258))  # pattern right
    pattern_3.add_vertex((430, 255))  # pattern down
    pattern_3.filled = True
    pattern_3.fill_color = "slategrey"
    pattern_3.color = "slategrey"
    window.add(pattern_3)

    pattern_4 = GPolygon()
    pattern_4.add_vertex((450, 255))  # pattern left
    pattern_4.add_vertex((475, 240))  # pattern up
    pattern_4.add_vertex((500, 255))  # pattern right
    pattern_4.add_vertex((475, 245))  # pattern down
    pattern_4.filled = True
    pattern_4.fill_color = "slategrey"
    pattern_4.color = "slategrey"
    window.add(pattern_4)

    pattern_5 = GPolygon()
    pattern_5.add_vertex((505, 255))  # pattern left
    pattern_5.add_vertex((530, 240))  # pattern up
    pattern_5.add_vertex((555, 255))  # pattern right
    pattern_5.add_vertex((530, 245))  # pattern down
    pattern_5.filled = True
    pattern_5.fill_color = "slategrey"
    pattern_5.color = "slategrey"
    window.add(pattern_5)

    pattern_6 = GPolygon()
    pattern_6.add_vertex((555, 260))  # pattern left
    pattern_6.add_vertex((575, 250))  # pattern up
    pattern_6.add_vertex((605, 265))  # pattern right
    pattern_6.add_vertex((575, 255))  # pattern down
    pattern_6.filled = True
    pattern_6.fill_color = "slategrey"
    pattern_6.color = "slategrey"
    window.add(pattern_6)

    l_beard_1 = GArc(200, 80, 0, 100, x=300, y=140)
    l_beard_1.color = "slategrey"
    window.add(l_beard_1)

    l_beard_2 = GArc(200, 50, 10, 150, x=330, y=155)
    l_beard_2.color = "slategrey"
    window.add(l_beard_2)

    l_beard_3 = GArc(200, 80, 30, 150, x=350, y=160)
    l_beard_3.color = "slategrey"
    window.add(l_beard_3)

    r_beard_1 = GArc(150, 90, 60, 120, x=560, y=145)
    r_beard_1.color = "slategrey"
    window.add(r_beard_1)

    r_beard_2 = GArc(150, 50, 30, 100, x=550, y=155)
    r_beard_2.color = "slategrey"
    window.add(r_beard_2)

    r_beard_3 = GArc(200, 80, 0, 100, x=530, y=160)
    r_beard_3.color = "slategrey"
    window.add(r_beard_3)

    l_eye_w = GOval(30, 30, x=430, y=130)
    l_eye_w.filled = True
    l_eye_w.fill_color = "snow"
    l_eye_w.color = "snow"
    window.add(l_eye_w)

    l_eye_b = GOval(15, 15, x=437, y=137)
    l_eye_b.filled = True
    l_eye_b.fill_color = "black"
    l_eye_b.color = "black"
    window.add(l_eye_b)

    r_eye_w = GOval(30, 30, x=540, y=130)
    r_eye_w.filled = True
    r_eye_w.fill_color = "snow"
    r_eye_w.color = "snow"
    window.add(r_eye_w)

    r_eye_b = GOval(15, 15, x=547, y=137)
    r_eye_b.filled = True
    r_eye_b.fill_color = "black"
    r_eye_b.color = "black"
    window.add(r_eye_b)

    mouth = GPolygon()
    mouth.add_vertex((425, 165))  # mouth left
    mouth.add_vertex((495, 162))  # mouth up
    mouth.add_vertex((570, 165))  # mouth right
    mouth.add_vertex((500, 180))  # mouth right down
    mouth.add_vertex((495, 180))  # mouth down
    mouth.add_vertex((490, 180))  # mouth left down
    mouth.filled = True
    mouth.fill_color = "snow"
    mouth.color = "snow"
    window.add(mouth)

    mouth_1 = GLine(450, 162, 450, 180)
    mouth_1.color = "slategrey"
    window.add(mouth_1)

    mouth_2 = GLine(475, 162, 475, 180)
    mouth_2.color = "slategrey"
    window.add(mouth_2)

    mouth_3 = GLine(500, 162, 500, 182)
    mouth_3.color = "slategrey"
    window.add(mouth_3)

    mouth_4 = GLine(530, 162, 530, 180)
    mouth_4.color = "slategrey"
    window.add(mouth_4)

    mouth_4 = GLine(550, 162, 550, 180)
    mouth_4.color = "slategrey"
    window.add(mouth_4)

    nose = GPolygon()
    nose.add_vertex((487, 145))  # nose left
    nose.add_vertex((507, 145))  # nose right
    nose.add_vertex((497, 150))  # nose down
    nose.filled = True
    nose.fill_color = "black"
    window.add(nose)


    l_foot_1 = GOval(60, 80, x=400, y=340)
    l_foot_1.filled = True
    l_foot_1.fill_color = "slategrey"
    l_foot_1.color = "slategrey"
    window.add(l_foot_1)

    l_foot_2 = GOval(50, 50, x=405, y=365)
    l_foot_2.filled = True
    l_foot_2.fill_color = "slategrey"
    l_foot_2.color = "grey"
    window.add(l_foot_2)

    l_foot_3 = GArc(20, 80, 90, 80, x=415, y=355)
    l_foot_3.filled = True
    l_foot_3.fill_color = "grey"
    l_foot_3.color = "grey"
    window.add(l_foot_3)

    l_foot_4 = GArc(20, 80, 90, 80, x=425, y=355)
    l_foot_4.filled = True
    l_foot_4.fill_color = "grey"
    l_foot_4.color = "grey"
    window.add(l_foot_4)

    l_foot_5 = GArc(20, 80, 90, 80, x=435, y=355)
    l_foot_5.filled = True
    l_foot_5.fill_color = "grey"
    l_foot_5.color = "grey"
    window.add(l_foot_5)

    r_foot_1 = GOval(60, 80, x=545, y=340)
    r_foot_1.filled = True
    r_foot_1.fill_color = "slategrey"
    r_foot_1.color = "slategrey"
    window.add(r_foot_1)

    r_foot_2 = GOval(50, 50, x=550, y=365)
    r_foot_2.filled = True
    r_foot_2.fill_color = "slategrey"
    r_foot_2.color = "grey"
    window.add(r_foot_2)

    r_foot_3 = GArc(20, 80, 90, 80, x=560, y=355)
    r_foot_3.filled = True
    r_foot_3.fill_color = "grey"
    r_foot_3.color = "grey"
    window.add(r_foot_3)

    r_foot_4 = GArc(20, 80, 90, 80, x=570, y=355)
    r_foot_4.filled = True
    r_foot_4.fill_color = "grey"
    r_foot_4.color = "grey"
    window.add(r_foot_4)

    r_foot_5 = GArc(20, 80, 90, 80, x=580, y=355)
    r_foot_5.filled = True
    r_foot_5.fill_color = "grey"
    r_foot_5.color = "grey"
    window.add(r_foot_5)


if __name__ == '__main__':
    main()
