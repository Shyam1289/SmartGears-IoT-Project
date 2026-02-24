// Digital twin storage for all workers
const digitalTwins = {
  1: { history: [] },
  2: { history: [] },
  3: { history: [] }
};

// Generate fake sensor data for all sensors
function generateWorkerData(workerId) {
  const heartRate = Math.floor(60 + Math.random() * 60);
  const bodyTemp = (36 + Math.random() * 2).toFixed(1);
  const gas = Math.floor(100 + Math.random() * 400);
  const ambientTemp = (25 + Math.random() * 10).toFixed(1);
  const humidity = Math.floor(40 + Math.random() * 40);
  const motion = Math.random() > 0.1 ? "Normal" : "Fall Detected";

  let risk = "Safe";
  if (heartRate > 100 || gas > 300) risk = "Warning";
  if (heartRate > 120 || gas > 400 || motion !== "Normal") risk = "Critical";

  return {
    workerId,
    heartRate,
    bodyTemp,
    gas,
    ambientTemp,
    humidity,
    motion,
    risk
  };
}

// Update digital twin state and history
function updateDigitalTwin(workerId) {
  const data = generateWorkerData(workerId);

  digitalTwins[workerId].current = data;

  digitalTwins[workerId].history.push({
    time: new Date().toLocaleTimeString(),
    heartRate: data.heartRate,
    bodyTemp: data.bodyTemp,
    gas: data.gas,
    ambientTemp: data.ambientTemp,
    humidity: data.humidity
  });

  // Keep last 30 readings for better visibility
  if (digitalTwins[workerId].history.length > 30) {
    digitalTwins[workerId].history.shift();
  }

  return digitalTwins[workerId];
}