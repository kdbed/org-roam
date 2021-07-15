using Luxor
P1  = Point(-200, 0)
CP1 = Point(-100, -100)
CP2 = Point(100, -100)
P2  = Point(200, 0)
@png begin
    circle.([P1, CP1, CP2, P2], 5, :fill)
    label.(["P1", "CP1", "CP2", "P2"], :N, [P1, CP1, CP2, P2], offset=10)
end 800 300 "../gitstage/visualization/julia/figs/fourpoints.png"

using Colors
@png begin
    sethue("red")
    label.(["P1", "CP1", "CP2", "P2"], :N, [P1, CP1, CP2, P2])
    line(P1, CP1,:stroke)
    line(CP2, P2,:stroke)
    sethue("black")
    move(P1)
    curve(CP1, CP2, P2)
    strokepath()
    circle.([P1, CP1, CP2, P2], 3, :fill)
end 800 300 "../gitstage/visualization/julia/figs/curve.png"


@png begin
    P1  = Point(-200, 0)
    CP1 = Point(-100, -100)
    CP2 = Point(100, -100)
    P2  = Point(200, 0)

    sethue("red")
    label.(["P1", "CP1", "CP2", "P2"], :N, [P1, CP1, CP2, P2])
    line(P1, CP1,:stroke)
    line(P2, CP2,:stroke)
    sethue("black")

    beziersegment = BezierPathSegment(P1, CP1, CP2, P2)
    circle.(beziersegment, 3, :fill)
    drawbezierpath(beziersegment, :stroke)
end 800 250 "../gitstage/visualization/julia/figs/drawbezierpath.png"


@png begin
    sethue("red")
    triangle = ngon(O, 120, 3, vertices=true)
    poly(triangle, :stroke, close=true)

    sethue("black")
    bezierpath = makebezierpath(triangle)
    drawbezierpath(bezierpath, :stroke)
    circle.(triangle, 5, :fill)

    for bps in bezierpath
        circle.(bps, 3, :fill)
        line(bps[1], bps[2], :stroke)
        line(bps[3], bps[4], :stroke)
    end

    label.(["p1", "p2", "p3"], [:S, :NW, :E], triangle, offset=10)
end 400 300 "../gitstage/visualization/julia/figs/makebezierpath.png"



function frame(scene, framenumber)
    background("white")
    eased_n = scene.easingfunction(framenumber, 0, 1, scene.framerange.stop)
    sethue("red")
    triangle = ngon(O, 120, 3, vertices=true)
    poly(triangle, :stroke, close=true)
    sethue("black")
    bezierpath = makebezierpath(triangle)
    newbezierpath = BezierPath()
    for bps in bezierpath
        push!(newbezierpath,
            BezierPathSegment(bps.p1,
             between(bps.cp1, bps.p1, eased_n),
             between(bps.cp2, bps.p2, eased_n),
             bps.p2))
    end
    for bps in newbezierpath
        circle.(bps, 3, :fill)
        line(bps.p1, bps.cp1, :stroke)
        line(bps.cp2, bps.p2, :stroke)
    end
    drawbezierpath(newbezierpath, :stroke)
end

width, height = (256, 256)

bedtimemovie = Movie(width, height, "bedtimemovie")
# probably requires ffmpeg installed
animate(bedtimemovie, [Scene(bedtimemovie, frame, 1:150, easingfunction=easeoutquad)], creategif=true, framerate=30, pathname="../gitstage/visualization/julia/figs/bedtimemovie.gif")
