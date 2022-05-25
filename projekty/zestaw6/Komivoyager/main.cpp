#include <iostream>
#include <fstream>
#include <vector>
#include <utility>
#include <cmath>
#include <cstdlib>
#include <ctime>

using namespace std;

struct Point
{
  double x;
  double y;
  /// ctor
  Point(double nx, double ny)
  : x(nx), y(ny)
  {

  }

  /// copy ctor
  Point(const Point& other)
  : x(other.x), y(other.y)
  {

  }
};

void swapABCD(std::vector<Point>& points, const unsigned b, const unsigned c)
{
  if(b<c)
  {
    std::swap(points[b], points[c]);
    if(c-b > 2) // if there is more than one element in between then swap their order
    {
      std::vector<Point> middle(&points[b+1], &points[c]);
      auto itrP = points.begin() + b + 1;
      for(auto itrM = middle.rbegin(); itrM!=middle.rend(); ++itrM)
      {
        *itrP = *itrM;
        ++itrP;
      }
    }

  }
}

double totalDistS(std::vector<Point>& points)
{
  auto last = points.begin();
  double dists = 0.0;
  for(auto itr = points.begin()+1; itr!=points.end(); ++itr)
  {
    dists += ((*itr).x - (*last).x)*((*itr).x - (*last).x) + ((*itr).y - (*last).y)*((*itr).y - (*last).y);
    ++last;
  }
  dists += (points[0].x - (*last).x)*(points[0].x - (*last).x) + (points[0].y - (*last).y)*(points[0].y - (*last).y);
  return dists;
}

double distS(std::vector<Point>& points, const unsigned a, const unsigned b, const unsigned c, const unsigned d)
{
  double dists = 0.0;
  dists += (points[a].x - points[b].x)*(points[a].x - points[b].x)
        + (points[a].y - points[b].y)*(points[a].y - points[b].y);
  dists += (points[d].x - points[c].x)*(points[d].x - points[c].x)
        + (points[d].y - points[c].y)*(points[d].y - points[c].y);
  return dists;
}

const int rand_int(const int min, const int max)
{
  return (min + rand()%(max-min+1));
}

const float rand_float(const float min, const float max)
{
  return (min + (rand()/(1.0 * RAND_MAX)) *(max-min));
}

double simulatedAnnealing(std::vector<Point>& points, unsigned MAX_IT = 100000)
{
  srand(time(NULL));
  double current = totalDistS(points);
  unsigned N = points.size();
  for(unsigned i=100;i>=1;--i)
  {
    double T = 0.001*i*i;
    for (unsigned it = 0; it < MAX_IT; ++it)
    {
      // to prevent crossing and values check b and c are picked in order
      unsigned b = rand_int(1, N-2);
      unsigned c = b + rand_int(1, N-b-1);
      unsigned a = b-1;
      unsigned d = c+1==N ? 0 : c+1;
      double currabcd = distS(points, a, b, c, d);
      double newabcd = distS(points, a, c, b, d);

      if(currabcd > newabcd)
      {
        swapABCD(points, b, c);
        current += -currabcd + newabcd;
      }
      else
      {
        float r = rand_float(0.0f, 1.0f);
        if(r < std::exp(-(newabcd-currabcd)/T))
        {
          swapABCD(points, b, c);
          current += -currabcd + newabcd;
        }
      }

    }
  }
  return current;
}


int main()
{
    std::ifstream data("input_150.dat");
    std::vector<Point> points;
    while (!data.eof())
    {
      double x, y;
      data>>x>>y;
      points.push_back(Point(x, y));
    }
    points.pop_back(); // last one is read twice
    data.close();
    std::cout<<"Total: "<<points.size()<<std::endl;
    for (auto& p : points )
      std::cout << "x: " << p.x << " y: " << p.y << "\n";
    std::cout<<"Distance: "<<totalDistS(points)<<std::endl;
    std::cout<<"Distance(Komi): "<<simulatedAnnealing(points)<<std::endl;
    std::ofstream output("output.csv");
    for (auto& p : points )
      output << p.x << ";" << p.y << "\n";
    output<<std::endl;
    output.close();
    return 0;
}
