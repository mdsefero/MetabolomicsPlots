import plotly.plotly as py
from plotly.graph_objs import *
py.sign_in('mdsefero', 'iNOab4LSemLB7jBCmTo8')
trace1 = {
  "x": [0.689484, 0.476483, 0.58677, 1.068768, 1.43806, 1.483567, 1.163844, 1.491083, 1.970356, 1.961689, 1.823355, 1.868743, 1.437345, 1.248269, 1.108745, 1.670774, 1.503391, 1.406028, 1.97107, 1.853437, 1.361601, 1.139926, 1.949556, 2.323108, 2.558936, 2.650508, 2.431305, 2.026224, 1.971259, 1.168452, 1.342775, 1.129037, 0.871781, 0.855148, 0.395625, 1.051331, 1.309558, 1.876837, 2.620561, 2.508878, 2.646833, 2.448341, 1.610501, 1.925691, 1.9184, 1.910517, 2.450736, 2.381144, 2.1596, 2.379856, 2.254824, 2.32, 1.698536, 1.527831, 1.530377, 1.67204, 1.534793, 1.886021, 2.062097, 2.128729, 2.057646, 2.155564, 2.698137, 3.066121, 3.925938, 4.240422, 3.907132, 3.750647, 2.918651, 2.980647, 2.992436, 2.71034, 2.693541, 2.361263, 1.897547, 2.345557, 2.007566, 1.599818, 1.182395, 1.469907, 1.460792, 1.11318, 0.879555, 1.351152, 1.392628, 1.926062, 1.211311, 0.913065, 1.363192, 2.032102, 1.738637, 1.249448, 0.610179, 0.853197, 0.794531, 0.635271, 0.545627, 0.137978, 0.552325, 0.417952, 0.063636, 0.270569, 0.465861, 0.224424, 0.234005, 0.066304, -0.590007, -0.564228, -0.862183, -0.835138, -0.358328, -0.153771, -0.402331, -0.288023, -0.076669, -0.314785, 0.038873, -0.373976, -0.305032, -0.325419, 0.261204, 1.198158, 0.95516, -0.054643, 0.170616, 0.44983, 0.033248, 0.321234, 0.299138, 0.498764, 1.114521, 0.63712, 0.938266, 1.321346, 1.293162, 1.50869, 1.913274, 1.765946, 2.040353, 1.381556, 0.174465, 0.028495, 0.379481, -0.669148, -0.534714, -0.886413, -1.721495, -1.00214, -1.919706, -1.140082, -1.305455, -1.385275, -1.700804, -1.383739, -1.418135, -1.316977, -1.209985, -1.627034, -1.867307, -2.198017, -2.421694, -2.415605, -2.724491, -2.008271, -1.465631, -1.626449, -1.340794, -1.017376, -0.71625, -0.617038, -0.551376, -0.184614, -0.081288, 0.485871, 0.984442, 0.695647, 0.089495, -0.321205, -0.967925, -1.118629, -1.550979, -2.283605, -1.755864, -2.054186, -1.970629, -1.417753, -1.710782, -0.79207, -0.956221, -1.288402, -2.311384, -1.980432, -2.813299, -2.345587, -2.111185, -2.290606, -2.656762, -2.373667, -2.454531, -1.968977], 
  "y": [-0.014459, 0.162624, 0.102149, 0.678668, 0.683633, 0.140479, 0.125522, 0.31764, 0.389628, 0.144644, 0.309693, 0.171245, 0.781093, 0.429151, 0.233132, -0.080785, -0.179939, 0.025858, 0.309369, 0.65834, 0.443953, 1.295734, 1.032481, 0.66557, 0.22719, 0.817791, 1.189158, 1.167509, 0.499964, 0.683057, 0.672141, 0.183479, 0.06947, 0.587134, 0.606762, 0.804046, 0.67245, 0.506276, 0.556901, 0.445584, 0.160679, -0.003327, 0.031129, -0.412504, -0.344678, -0.246417, -0.725501, -1.214003, -1.524586, -1.845657, -1.268736, -1.171255, -1.233225, -1.374688, -1.35563, -1.146433, -1.167195, -0.864813, -0.488551, 0.153843, 0.302593, 0.568636, 0.182249, 0.56296, 0.252966, -0.220912, -0.328587, -0.193345, -0.238123, 0.261956, 0.081961, -0.49059, -0.259896, -0.187197, -0.032457, 0.049672, 0.12171, -0.105825, -0.745416, -0.795117, -0.45044, -0.514758, -0.639992, -0.329654, -0.215191, -0.37535, -1.208597, -1.064432, -1.33837, -1.405084, -1.456743, -1.299677, -1.236958, -0.482796, -0.346327, -0.689043, -0.840409, -1.16441, -1.242295, -1.794645, -1.392008, -1.760419, -2.329245, -2.168251, -1.890062, -2.254005, -2.074276, -2.180494, -2.411982, -2.001141, -2.011921, -1.745932, -1.553359, -1.88065, -1.859422, -1.519305, -1.148978, -1.561826, -1.189923, -1.093044, -0.90863, -0.709813, -0.866599, -0.849581, -0.818985, -0.295839, -0.426162, -0.342447, -0.219997, -0.515553, -0.494993, -0.680155, -1.230975, -0.900911, -0.76587, -0.695327, -0.904249, -0.91563, -1.337914, -1.929364, -2.5407, -2.366009, -1.975778, -1.711153, -1.548458, -1.547606, -1.398594, -0.855336, -1.261225, -1.693494, -1.940874, -1.513315, -1.454906, -1.487379, -1.296192, -1.051611, -1.301749, -0.881364, -1.073767, -1.046423, -1.381144, -1.391328, -1.006637, -1.0177, -0.95663, -1.079294, -1.054864, -0.987401, -0.671692, -0.737152, -0.769002, -0.613152, -0.695816, -0.376302, -0.394376, -0.137996, -0.432969, -0.605479, -0.710437, -0.92498, -0.436884, -0.8949, -1.162008, -0.540825, -0.637033, -0.917763, -0.529252, -0.311093, -0.476337, 0.24526, 0.293434, -0.17767, -0.389484, -0.311234, -0.097245, -0.760096, -0.203731, -0.155186, -0.091853, 0.342108], 
  "z": [0.428751, 0.449488, 0.769481, 1.023915, 0.752397, 1.389489, 1.098527, 0.760376, 0.631279, 0.254462, 0.151225, -0.160235, -0.56967, -0.795403, -0.744953, -0.820339, -0.791839, -0.96783, -0.65142, -0.66108, -0.126488, 0.114152, 0.417303, 0.615544, 0.385185, 0.186861, -0.0858, -0.120976, -0.035002, -0.309909, -0.208439, -0.485355, -0.734185, -0.574637, -1.004597, -1.250838, -1.174746, -1.376205, -1.528117, -1.501028, -1.605397, -1.875326, -2.069439, -2.138976, -2.29942, -2.245133, -2.82832, -2.812268, -2.873087, -2.758474, -3.020816, -3.604322, -3.369023, -3.394583, -3.29579, -3.038195, -3.646896, -3.52345, -3.273344, -3.081451, -2.701675, -2.718267, -2.875416, -2.909034, -3.011479, -2.79574, -2.430246, -2.166711, -2.143549, -2.218529, -2.173249, -1.838208, -1.613949, -1.208869, -0.792615, -1.164745, -1.080368, -1.08692, -0.878417, -0.562867, -0.599801, -0.508419, -0.672436, -0.829762, -0.596751, -0.554818, -0.556275, -0.494078, -0.238343, -0.335621, 0.028875, 0.10227, 0.31525, 0.164532, -0.462431, -0.492473, -0.344744, -0.537114, -0.476395, -0.288381, -0.495803, -0.027581, 0.035753, -0.19307, 0.136462, 0.006976, -0.46601, -0.12312, -0.028077, 0.037551, -0.136263, -0.246048, -0.313232, -0.271885, -0.312956, -0.132629, 0.096291, 0.11155, -0.133022, -0.228238, -0.426471, -0.421499, -0.542272, -0.459668, -0.482471, -0.534499, -0.397172, -0.372978, -0.136276, -0.431687, -0.075384, -0.358235, -0.003075, -0.195531, -0.375611, -0.218006, 0.365808, 0.263471, 0.586506, 0.389045, 0.315377, 0.128681, -0.269045, -0.162167, -0.336419, -0.019438, 0.231251, 0.02658, 0.190797, 0.737523, 0.32612, 0.310784, 0.596005, 0.37976, 0.044075, 0.239119, 0.251076, 0.218926, -0.028889, 0.155034, 0.187969, 0.38736, -0.038025, -0.095609, -0.028786, 0.100394, -0.231481, 0.016533, -0.217537, -0.297303, -0.232595, -0.177161, -0.583397, -1.082045, -0.701239, -0.589993, -0.751204, -0.800903, -1.191601, -0.601275, -0.199922, -0.649577, -0.712762, -0.140276, -0.296211, -0.255914, -0.141535, -0.398747, -0.717366, -1.040109, -1.061344, -1.414031, -1.394257, -1.003791, -0.825758, -1.086674, -1.190057, -1.466129, -1.915351, -1.952409], 
  "marker": {
    "color": "#458B00", 
    "size": 2
  }, 
  "mode": "markers", 
  "name": "", 
  "type": "scatter3d"
}
trace2 = {
  "x": [0.689484, 0.476483, 0.58677, 1.068768, 1.43806, 1.483567, 1.163844, 1.491083, 1.970356, 1.961689, 1.823355, 1.868743, 1.437345, 1.248269, 1.108745, 1.670774, 1.503391, 1.406028, 1.97107, 1.853437, 1.361601, 1.139926, 1.949556, 2.323108, 2.558936, 2.650508, 2.431305, 2.026224, 1.971259, 1.168452, 1.342775, 1.129037, 0.871781, 0.855148, 0.395625, 1.051331, 1.309558, 1.876837, 2.620561, 2.508878, 2.646833, 2.448341, 1.610501, 1.925691, 1.9184, 1.910517, 2.450736, 2.381144, 2.1596, 2.379856, 2.254824, 2.32, 1.698536, 1.527831, 1.530377, 1.67204, 1.534793, 1.886021, 2.062097, 2.128729, 2.057646, 2.155564, 2.698137, 3.066121, 3.925938, 4.240422, 3.907132, 3.750647, 2.918651, 2.980647, 2.992436, 2.71034, 2.693541, 2.361263, 1.897547, 2.345557, 2.007566, 1.599818, 1.182395, 1.469907, 1.460792, 1.11318, 0.879555, 1.351152, 1.392628, 1.926062, 1.211311, 0.913065, 1.363192, 2.032102, 1.738637, 1.249448, 0.610179, 0.853197, 0.794531, 0.635271, 0.545627, 0.137978, 0.552325, 0.417952, 0.063636, 0.270569, 0.465861, 0.224424, 0.234005, 0.066304, -0.590007, -0.564228, -0.862183, -0.835138, -0.358328, -0.153771, -0.402331, -0.288023, -0.076669, -0.314785, 0.038873, -0.373976, -0.305032, -0.325419, 0.261204, 1.198158, 0.95516, -0.054643, 0.170616, 0.44983, 0.033248, 0.321234, 0.299138, 0.498764, 1.114521, 0.63712, 0.938266, 1.321346, 1.293162, 1.50869, 1.913274, 1.765946, 2.040353, 1.381556, 0.174465, 0.028495, 0.379481, -0.669148, -0.534714, -0.886413, -1.721495, -1.00214, -1.919706, -1.140082, -1.305455, -1.385275, -1.700804, -1.383739, -1.418135, -1.316977, -1.209985, -1.627034, -1.867307, -2.198017, -2.421694, -2.415605, -2.724491, -2.008271, -1.465631, -1.626449, -1.340794, -1.017376, -0.71625, -0.617038, -0.551376, -0.184614, -0.081288, 0.485871, 0.984442, 0.695647, 0.089495, -0.321205, -0.967925, -1.118629, -1.550979, -2.283605, -1.755864, -2.054186, -1.970629, -1.417753, -1.710782, -0.79207, -0.956221, -1.288402, -2.311384, -1.980432, -2.813299, -2.345587, -2.111185, -2.290606, -2.656762, -2.373667, -2.454531, -1.968977], 
  "y": [-0.014459, 0.162624, 0.102149, 0.678668, 0.683633, 0.140479, 0.125522, 0.31764, 0.389628, 0.144644, 0.309693, 0.171245, 0.781093, 0.429151, 0.233132, -0.080785, -0.179939, 0.025858, 0.309369, 0.65834, 0.443953, 1.295734, 1.032481, 0.66557, 0.22719, 0.817791, 1.189158, 1.167509, 0.499964, 0.683057, 0.672141, 0.183479, 0.06947, 0.587134, 0.606762, 0.804046, 0.67245, 0.506276, 0.556901, 0.445584, 0.160679, -0.003327, 0.031129, -0.412504, -0.344678, -0.246417, -0.725501, -1.214003, -1.524586, -1.845657, -1.268736, -1.171255, -1.233225, -1.374688, -1.35563, -1.146433, -1.167195, -0.864813, -0.488551, 0.153843, 0.302593, 0.568636, 0.182249, 0.56296, 0.252966, -0.220912, -0.328587, -0.193345, -0.238123, 0.261956, 0.081961, -0.49059, -0.259896, -0.187197, -0.032457, 0.049672, 0.12171, -0.105825, -0.745416, -0.795117, -0.45044, -0.514758, -0.639992, -0.329654, -0.215191, -0.37535, -1.208597, -1.064432, -1.33837, -1.405084, -1.456743, -1.299677, -1.236958, -0.482796, -0.346327, -0.689043, -0.840409, -1.16441, -1.242295, -1.794645, -1.392008, -1.760419, -2.329245, -2.168251, -1.890062, -2.254005, -2.074276, -2.180494, -2.411982, -2.001141, -2.011921, -1.745932, -1.553359, -1.88065, -1.859422, -1.519305, -1.148978, -1.561826, -1.189923, -1.093044, -0.90863, -0.709813, -0.866599, -0.849581, -0.818985, -0.295839, -0.426162, -0.342447, -0.219997, -0.515553, -0.494993, -0.680155, -1.230975, -0.900911, -0.76587, -0.695327, -0.904249, -0.91563, -1.337914, -1.929364, -2.5407, -2.366009, -1.975778, -1.711153, -1.548458, -1.547606, -1.398594, -0.855336, -1.261225, -1.693494, -1.940874, -1.513315, -1.454906, -1.487379, -1.296192, -1.051611, -1.301749, -0.881364, -1.073767, -1.046423, -1.381144, -1.391328, -1.006637, -1.0177, -0.95663, -1.079294, -1.054864, -0.987401, -0.671692, -0.737152, -0.769002, -0.613152, -0.695816, -0.376302, -0.394376, -0.137996, -0.432969, -0.605479, -0.710437, -0.92498, -0.436884, -0.8949, -1.162008, -0.540825, -0.637033, -0.917763, -0.529252, -0.311093, -0.476337, 0.24526, 0.293434, -0.17767, -0.389484, -0.311234, -0.097245, -0.760096, -0.203731, -0.155186, -0.091853, 0.342108], 
  "z": [0.428751, 0.449488, 0.769481, 1.023915, 0.752397, 1.389489, 1.098527, 0.760376, 0.631279, 0.254462, 0.151225, -0.160235, -0.56967, -0.795403, -0.744953, -0.820339, -0.791839, -0.96783, -0.65142, -0.66108, -0.126488, 0.114152, 0.417303, 0.615544, 0.385185, 0.186861, -0.0858, -0.120976, -0.035002, -0.309909, -0.208439, -0.485355, -0.734185, -0.574637, -1.004597, -1.250838, -1.174746, -1.376205, -1.528117, -1.501028, -1.605397, -1.875326, -2.069439, -2.138976, -2.29942, -2.245133, -2.82832, -2.812268, -2.873087, -2.758474, -3.020816, -3.604322, -3.369023, -3.394583, -3.29579, -3.038195, -3.646896, -3.52345, -3.273344, -3.081451, -2.701675, -2.718267, -2.875416, -2.909034, -3.011479, -2.79574, -2.430246, -2.166711, -2.143549, -2.218529, -2.173249, -1.838208, -1.613949, -1.208869, -0.792615, -1.164745, -1.080368, -1.08692, -0.878417, -0.562867, -0.599801, -0.508419, -0.672436, -0.829762, -0.596751, -0.554818, -0.556275, -0.494078, -0.238343, -0.335621, 0.028875, 0.10227, 0.31525, 0.164532, -0.462431, -0.492473, -0.344744, -0.537114, -0.476395, -0.288381, -0.495803, -0.027581, 0.035753, -0.19307, 0.136462, 0.006976, -0.46601, -0.12312, -0.028077, 0.037551, -0.136263, -0.246048, -0.313232, -0.271885, -0.312956, -0.132629, 0.096291, 0.11155, -0.133022, -0.228238, -0.426471, -0.421499, -0.542272, -0.459668, -0.482471, -0.534499, -0.397172, -0.372978, -0.136276, -0.431687, -0.075384, -0.358235, -0.003075, -0.195531, -0.375611, -0.218006, 0.365808, 0.263471, 0.586506, 0.389045, 0.315377, 0.128681, -0.269045, -0.162167, -0.336419, -0.019438, 0.231251, 0.02658, 0.190797, 0.737523, 0.32612, 0.310784, 0.596005, 0.37976, 0.044075, 0.239119, 0.251076, 0.218926, -0.028889, 0.155034, 0.187969, 0.38736, -0.038025, -0.095609, -0.028786, 0.100394, -0.231481, 0.016533, -0.217537, -0.297303, -0.232595, -0.177161, -0.583397, -1.082045, -0.701239, -0.589993, -0.751204, -0.800903, -1.191601, -0.601275, -0.199922, -0.649577, -0.712762, -0.140276, -0.296211, -0.255914, -0.141535, -0.398747, -0.717366, -1.040109, -1.061344, -1.414031, -1.394257, -1.003791, -0.825758, -1.086674, -1.190057, -1.466129, -1.915351, -1.952409], 
  "alphahull": 10.0, 
  "color": "90EE90", 
  "name": "", 
  "opacity": 0.15, 
  "type": "mesh3d"
}
data = Data([trace1, trace2])
layout = {
  "height": 500, 
  "scene": {
    "xaxis": {
      "range": [-2.85, 4.25], 
      "tickvals": [-1.1, 0.7, 2.5, 4.2], 
      "zeroline": False
    }, 
    "yaxis": {
      "range": [-2.65, 1.32], 
      "tickvals": [-1.3, 0.0, 1.3], 
      "zeroline": False
    }, 
    "zaxis": {
      "range": [-3.67, 1.4], 
      "tickvals": [-3.7, -2.4, -1.1, 0.1, 1.4], 
      "zeroline": False
    }
  }, 
  "title": "Alpha shape of a set of 3D points. Alpha=0.1", 
  "width": 500
}
fig = Figure(data=data, layout=layout)
plot_url = py.plot(fig)