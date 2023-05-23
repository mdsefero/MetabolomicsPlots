import plotly.plotly as py
import plotly.graph_objs as go
py.sign_in('mdsefero', 'iNOab4LSemLB7jBCmTo8')

import numpy as np

#x, y, z = np.random.multivariate_normal(np.array([0,0,0]), np.eye(3), 200).transpose()

#set dot size
s = 10


#BONE HFD
x, y, z = np.array([(-409680000,-448620000,-439660000,-433520000,-446420000,-411420000,-408980000,-402370000), (-112980000,-81387000,-102410000,-100780000,-84406000,-129840000,-88071000,-124790000), (71315000,86046000,79224000,79295000,82891000,61799000,79079000,65132000,)])#, np.eye(3), 200,#.transpose()
trace1 = go.Scatter3d(
    x=x,
    y=y,
    z=z,
    mode='markers',
    marker=dict(
		color='rgb(44, 160, 44)',
        size=s,
        line=dict(
            color='rgba(44, 160, 44, 0.14)',
            width=0.5
        ),
        opacity=0.8
    )
)


#BONE CONTROL 
x2, y2, z2 = np.array([(-416330000,-391910000,-440290000,-422300000,-429880000,-439710000,-440800000,-409120000,), (-119140000,-109330000,-88021000,-124800000,-86621000,-86098000,-75289000,-100920000,), (73366000,76024000,82033000,70121000,85133000,87833000,91659000,77815000,)])#, np.eye(3), 200,#.transpose()
trace2 = go.Scatter3d(
    x=x2,
    y=y2,
    z=z2,
    mode='markers',
    marker=dict(
        color='rgb(152, 223, 138)',
        size=s,
        symbol='circle',
        line=dict(
            color='rgb(152, 223, 138)',
            width=1
        ),
        opacity=0.9
    )
)

#LIVER HFD
x3, y3, z3 = np.array([(-20798000,-65029000,-38399000,-69415000,-81977000,-122260000,-104380000,-269720000), (49654000,2220000,80839000,70567000,6990600,60689000,16720000,5934700), (-285080000,-299500000,-55618000,-188930000,-308860000,-249390000,-291760000,-191010000)])#, np.eye(3), 200,#.transpose()
trace3 = go.Scatter3d(
    x=x3,
    y=y3,
    z=z3,
    mode='markers',
    marker=dict(
		color='rgb(31, 119, 180)',
        size=s,
        line=dict(
            color='rgba(31, 119, 180, 0.14)',
            width=0.5
        ),
        opacity=0.8
    )
)

#LIVER CONTROL
x4, y4, z4 = np.array([(-122880000,-99240000,-34047000,-29240000,-94774000,-132690000,-172390000,-126050000), (43130000,48590000,62350000,90501000,66108000,42620000,24165000,37470000), (-171890000,-208640000,-191200000,-102170000,-282070000,-340720000,-173040000,-153230000)])#, np.eye(3), 200,#.transpose()
trace4	= go.Scatter3d(
    x=x4,
    y=y4,
    z=z4,
    mode='markers',
    marker=dict(
		color='rgb(174, 199, 232)',
        size=s,
        line=dict(
            color='rgba(174, 199, 232, 0.14)',
            width=0.5
        ),
        opacity=0.8
    )
)
	
#MUSCLE HFD
x5, y5, z5 = np.array([(411050000,477780000,419130000,480160000,558780000,570380000,579640000,466240000), (-64567000,-90254000,-75842000,-94837000,-83571000,-93260000,-63752000,-83649000,), (25888000,10075000,16347000,7568500,12220000,6227100,15582000,16624000)])#, np.eye(3), 200,#.transpose()
trace5	= go.Scatter3d(
    x=x5,
    y=y5,
    z=z5,
    mode='markers',
    marker=dict(
		color='rgb(255, 127, 14)',
        size=s,
        line=dict(
            color='rgba(255, 127, 14, 0.14)',
            width=0.5
        ),
        opacity=0.8
    )
)

#MUSCLE CONTROL
x6, y6, z6 = np.array([(369160000,619340000,565360000,521370000,423660000,441310000,617270000,439910000), (-125560000,-74145000,-78445000,-100540000,-97703000,-101970000,-71283000,-94722000), (19533000,18671000,14778000,13265000,21714000,25667000,20755000,25739000)])#, np.eye(3), 200,#.transpose()
trace6	= go.Scatter3d(
    x=x6,
    y=y6,
    z=z6,
    mode='markers',
    marker=dict(
		color='rgb(255, 187, 120)',
        size=s,
        line=dict(
            color='rgba(255, 187, 120, 0.14)',
            width=0.5
        ),
        opacity=0.8
    )
)
	
#PLASMA HFD
x7, y7, z7 = np.array([(36289000,77577000,41528000,35297000,6788700,-11246000,6573000,42322000), (124710000,125040000,144700000,114890000,155340000,150440000,176170000,144710000), (116670000,108520000,123700000,105380000,112930000,123500000,132490000,138670000)])#, np.eye(3), 200,#.transpose()
trace7	= go.Scatter3d(
    x=x7,
    y=y7,
    z=z7,
    mode='markers',
    marker=dict(
		color='rgb(214, 39, 40)',
        size=s,
        line=dict(
            color='rgba(214, 39, 40, 0.14)',
            width=0.5
        ),
        opacity=0.8
    )
)

#PLASMA CONTROL 
x8, y8, z8 = np.array([(46884000,1443500,16632000,66644000,38534000,20815000,-16675000,4376900), (133600000,125460000,136850000,156350000,164140000,151160000,143430000,153450000,), (119320000,122430000,115880000,110810000,133230000,129680000,137810000,142670000,)])#, np.eye(3), 200,#.transpose()
trace8	= go.Scatter3d(
    x=x8,
    y=y8,
    z=z8,
    mode='markers',
    marker=dict(
		color='rgb(255, 152, 150)',
        size=s,
        line=dict(
            color='rgba(255, 152, 150, 0.14)',
            width=0.5
        ),
        opacity=0.8
    )
)
	
data = [trace1, trace2, trace3, trace4, trace5, trace6, trace7, trace8]
layout = go.Layout(
    margin=dict(
        l=0,
        r=0,
        b=0,
        t=0
    )
)
fig = go.Figure(data=data, layout=layout)
py.plot(fig, filename='simple-3d-scatter')