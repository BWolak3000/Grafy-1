#include <iostream>
#include <fstream>
#include <vector>
#include <utility>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <algorithm>
#include <random>

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
    auto pb = points.begin() + b;
    auto pc = points.begin() + c;
    for(unsigned i=0;i<(c-b+1)/2;++i)
    {
      std::swap(*pb, *pc);
      ++pb;
      --pc;
    }
  }
}

double totalDistS(std::vector<Point>& points)
{
  auto last = points.begin();
  double dists = 0.0;
  for(auto itr = points.begin()+1; itr!=points.end(); ++itr)
  {
    dists += sqrt(((*itr).x - (*last).x)*((*itr).x - (*last).x) + ((*itr).y - (*last).y)*((*itr).y - (*last).y));
    ++last;
  } 
  dists += sqrt((points[0].x - (*last).x)*(points[0].x - (*last).x) + (points[0].y - (*last).y)*(points[0].y - (*last).y));
  return dists;
}

double distS(std::vector<Point>& points, const unsigned a, const unsigned b, const unsigned c, const unsigned d)
{
  double dists = 0.0;
  dists += sqrt((points[a].x - points[b].x)*(points[a].x - points[b].x)
        + (points[a].y - points[b].y)*(points[a].y - points[b].y));
  dists += sqrt((points[d].x - points[c].x)*(points[d].x - points[c].x)
        + (points[d].y - points[c].y)*(points[d].y - points[c].y));
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

double simulatedAnnealing(std::vector<Point>& points, unsigned MAX_IT = 10000)
{
  srand(time(NULL));
  double current = totalDistS(points);
  unsigned N = points.size();
  for(unsigned i=200;i>=1;i = i - 1)
  {
    double T = 0.0001 *i*i*i;
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
    double d = 1894, temp;
    auto rng = std::default_random_engine {};
    std::cout<<"Distance: "<<totalDistS(points)<<std::endl;
    for(int i = 0; i < 30; i++){
      //std::cout<<"Attempt: " << i +1<<std::endl;
      
      std::cout<<"*";
      std::shuffle(std::begin(points), std::end(points), rng);
      //std::cout<<"shuffled"<<std::endl;
      temp = simulatedAnnealing(points);
      if (temp < d){
        d = temp;
        std::cout<<"Komi: "<<temp<<std::endl;
        std::ofstream output("output.csv");
        for (auto& p : points )
          output << p.x << ";" << p.y << "\n";
        output<<std::endl;
        output.close();
      }
    }
    return 0;
}
