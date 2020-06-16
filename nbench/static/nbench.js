function showBenchmark() {
    setActive = document.getElementById('Benchmarks');
    setActive.style.display = "inline";
    setActive.style.proerty = "luci-navigation__link--is-active";

    document.getElementById('Dashboard').style.display = "none";
    document.getElementById('Hosts').style.display = "none";
    document.getElementById('Workloads').style.display = "none";
    document.getElementById('WorkloadDesigner').style.display = "none";
}

function showHosts() {
    setActive = document.getElementById('Hosts');
    setActive.style.display = "inline";
    setActive.style.proerty = "luci-navigation__link--is-active";

    document.getElementById('Dashboard').style.display = "none";
    document.getElementById('Benchmarks').style.display = "none";
    document.getElementById('Workloads').style.display = "none";
    document.getElementById('WorkloadDesigner').style.display = "none";
}
function showDashboard() {
    document.getElementById('Dashboard').style.display = "inline";

    document.getElementById('Hosts').style.display = "none";
    document.getElementById('Benchmarks').style.display = "none";
    document.getElementById('Workloads').style.display = "none";
    document.getElementById('WorkloadDesigner').style.display = "none";
}
function showWorkloads() {
    setActive = document.getElementById('Workloads');
    setActive.style.display = "inline";
    setActive.style.proerty = "luci-navigation__link--is-active";

    document.getElementById('Dashboard').style.display = "none";
    document.getElementById('Hosts').style.display = "none";
    document.getElementById('Benchmarks').style.display = "none";
    document.getElementById('WorkloadDesigner').style.display = "none";
}

function showWorkloadDesigner() {
    setActive = document.getElementById('WorkloadDesigner');
    setActive.style.display = "inline";
    setActive.style.proerty = "luci-navigation__link--is-active";

    document.getElementById('Dashboard').style.display = "none";
    document.getElementById('Hosts').style.display = "none";
    document.getElementById('Benchmarks').style.display = "none";
    document.getElementById('Workloads').style.display = "none";
}

function showWorkArea(workArea) {
    let things = ["Workloads", "Hosts", "Benchmarks", "Dashboard", "WorkloadDesigner"];
    let thingLength = things.length;
    for (var i = 0; i < thingLength; i++) {
        if (workArea === things[i]) {
            console.log("Setting Work Area " + things[i] + " Active")
            document.getElementById(things[i]).style.display = "inline";
        } else {
            document.getElementById('Dashboard').style.display = "none";
            console.log("Setting Work Area " + things[i] + " Inactive")
        }
    }

}
