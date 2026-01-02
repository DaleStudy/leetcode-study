/**
(0,0) 에서 시작해서, 위 아래 끝값 및 왼쪽 오른쪽의 끝값을 갱신해가며
현재 위치가 이보다 커질 경우 각각을 -1 하고 방향을 바꿔준다.
 */
function spiralOrder(matrix: number[][]): number[] {
  let hmin = 0,
    hmax = matrix[0].length - 1,
    vmin = 0,
    vmax = matrix.length - 1;
  let x = 0,
    y = 0;
  const result = [];
  let currentStep = [1, 0];

  while (hmax >= hmin && vmax >= vmin) {
    result.push(matrix[y][x]);

    const next = applyCurrentStep(currentStep, x, y, hmin, hmax, vmin, vmax);
    currentStep = next.nextStep;
    x = next.x;
    y = next.y;
    hmin = next.hmin;
    hmax = next.hmax;
    vmin = next.vmin;
    vmax = next.vmax;

    // console.log(currentStep, x, y, hmin, hmax, vmin, vmax)
  }
  return result;
}

function applyCurrentStep(
  currentStep: number[],
  x: number,
  y: number,
  hmin: number,
  hmax: number,
  vmin: number,
  vmax: number
) {
  let nextStep = currentStep;

  switch (true) {
    case currentStep[0] === 1 && currentStep[1] === 0: {
      if (x >= hmax) {
        nextStep = [0, 1];
        y += 1;
        vmin += 1;
      } else {
        x += 1;
      }
      break;
    }
    case currentStep[0] === 0 && currentStep[1] === 1: {
      if (y >= vmax) {
        nextStep = [-1, 0];
        x -= 1;
        hmax -= 1;
      } else {
        y += 1;
      }
      break;
    }
    case currentStep[0] === -1 && currentStep[1] === 0: {
      if (hmin >= x) {
        nextStep = [0, -1];
        y -= 1;
        vmax -= 1;
      } else {
        x -= 1;
      }
      break;
    }
    case currentStep[0] === 0 && currentStep[1] === -1: {
      if (vmin >= y) {
        nextStep = [1, 0];
        x += 1;
        hmin += 1;
      } else {
        y -= 1;
      }
      break;
    }
  }
  return { nextStep, x, y, hmin, hmax, vmin, vmax };
}
